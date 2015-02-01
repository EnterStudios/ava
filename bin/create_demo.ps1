#region Configuration

# How many users to create
$UserCount = 150

# AD settings
$UPNSuffix = "@ava.test.domain"

# AD locations
$DomainRoot = "DC=ava,DC=test,DC=domain"
$CompanyRootOU = "Marvel Small"
$CompanyRootDN = "OU=$CompanyRootOU,$DomainRoot"

# Lists for offices and divisions
$CityList = "Avengers Mansion","Rikers Island","Stark Tower","Sanctum Sanctorum","Ravencroft","Asgard"
$DivisionList = "IT","Sales","Marketing","HR","Architecture","Operations","Development","Strategy","Finance","Administration","Security","Logistics","Customer Services","Research & Development","Market Development","Business Development","Management","Engineering","Infrastructure"

#endregion

#region Main script

Import-Module ActiveDirectory

# Don't separate array elements when converting to strings (default is a space)
$ofs = ''

Function Get-CrudePassword {
<#
.SYNOPSIS
Create a basic ASCII password.
.DESCRIPTION
A basic random password generator.
It will create a string of printable ASCII characters of the length specified that meets typical complexity requirements.
.PARAMETER Length
Character length of password to generate.
#>
    Param(
        [int]$Length = 15
    )

    do
    {
        $Password = [string](1..$Length | foreach { [Char](Get-Random -Min 32 -Max 126) })
    } until # Lazy complexity requirement check
        ($Password -cmatch '[A-Z]' -And
        $Password -cmatch '[a-z]' -And
        $Password -cmatch '\d')

    # Return as Secure String
    ConvertTo-SecureString $Password -AsPlainText -Force
}

Function Get-GroupInfo
{
    Param($City,$Division)
    $GroupName = "$City-$Division" -Replace ' '
    $GroupDescription="$Division in $City Access Group"

    # Return as custom object
    New-Object PSObject -Property @{
        Name = $Groupname
        Description = $GroupDescription
    }
}

# Create company base OU
New-ADOrganizationalUnit -Name $CompanyRootOU -Path $DomainRoot

# Create OUs for cities and divisions
foreach ($City in $CityList) 
{
    New-ADOrganizationalUnit -path $CompanyRootDN -name $City
    foreach ($Division in $DivisionList)
    {
        New-ADOrganizationalUnit -path "OU=$City,$CompanyRootDN" -name $Division

        # Create division group
        $GroupData = Get-GroupInfo -City $City -Division $Division
        New-ADGroup -Name $GroupData.Name -GroupScope Global -Description $GroupData.Description -Path "OU=$Division,OU=$City,$CompanyRootDN"
    }
}

# Select $UserCount random names from name list
# Only select names with two parts, and without possessive on first part (to exclude "So-and-so's twin")
$NameList = Get-Content names.txt | Where-Object { ($_ -Split ' ').Count -eq 2 -and ($_ -notmatch "^\S+'s ") } | Get-Random -Count $UserCount
# Keep track of existing usernames as new ones are created as they have to be unique
$Usernames = Get-ADObject -LDAPFilter "(&(objectclass=user)(objectcategory=person))" -Property samaccountname -SearchBase $DomainRoot -ResultPageSize 100 | Select-Object samaccountname

# Generate users from name list
foreach ($Name in $NameList) {
    $Firstname,$Lastname = $Name -Split " "
    $City = Get-Random $CityList
    $Division = Get-Random $DivisionList

    $LoginID = $Firstname[0] + $Lastname
    # Create SAM account name without invalid characters
    # Invalid characters: " [ ] : ; | = + * ? < > / \ ,
    # Cannot end with: .
    $sAMAccountName = [string]$LoginID[0..18] -Replace '("|\[|\]|:|;|\||=|\+|\*|\?|<|>|/|\\|,|\.$)'

    # Make sure name does not conflict
    if ($Usernames -contains $sAMAccountName) {
        $Counter = 0
        do {
            $CountLen = ([string]$Counter).Length
            $sAMAccountName = [string]$LoginID[0..(18-$CountLen)] + $Counter++
        } until ($Usernames -notcontains $sAMAccountName)
    }
    $Usernames += $sAMAccountName

    $userPrincipalName = $sAMAccountName + $UPNSuffix

    $ADPath = "OU=$Division,OU=$City,$CompanyRootDN"
    New-ADUser -Enabled $true -GivenName $Firstname -Surname $Lastname -DisplayName $Name -Name $Name -UserPrincipalName $userPrincipalName -Division $Division -City $City -Path $ADPath -SamAccountName $sAMAccountName -AccountPassword (Get-CrudePassword)

    # Add User to appropriate Security Group
    $Groupname = (Get-GroupInfo -City $City -Division $Division).Name
    Add-ADGroupmember $Groupname -Members $sAMAccountName
} 

#endregion