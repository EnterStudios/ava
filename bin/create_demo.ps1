#region Configuration

# Root OU below DomainRoot
$RootOUName = "Marvel Small"
#$RootOUName = "Marvel Medium"
#$RootOUName = "Marvel Large"

# DistinguishedName of Domain Root
$DomainRoot = "DC=ava,DC=test,DC=domain"

# Whatever the name of the $RootOUName Combined with Domain
$CompanyRootDN = "OU=$RootOUName,$DomainRoot"

# UPN Extension to the Domain
$UPNSuffix = "@ava.test.domain"

# List of Office Names
$CityList = "Avengers Mansion","Rikers Island","Stark Tower","Sanctum Sanctorum","Ravencroft","Asgard"

# List of Divisions Per Office
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

# Create base OU for Offices
New-ADOrganizationalUnit -name $RootOUName -path $DomainRoot

# Create OUs for cities and divisions
foreach ($City in $CityList) 
{
    New-ADOrganizationalUnit -path $CompanyRootDN -name $City
    foreach ($Division in $DivisionList)
    {
        New-ADOrganizationalUnit -path "OU=$City,$CompanyRootDN" -name $Division

        # Create division group
        $GroupData = Get-GroupInfo –City $City –Division $Division
        New-ADGroup -Name $GroupData.Name -GroupScope Global -Description $GroupData.Description -Path "OU=$Division,OU=$City,$CompanyRootDN"
    }
}

# Select 150 random names from name list
# Only select names with two parts, and without possessive on first part (to exclude "So-and-so's twin")
$NameList = Get-Content names.txt | Where-Object { ($_ -Split ' ').Count -eq 2 -and ($_ -notmatch "^\S+'s ") } | Get-Random -Count 150

# Generate users from name list
foreach ($Name in $NameList) {
    $Firstname,$Lastname = $Name.Split(" ")
    $City = Get-Random $CityList
    $Division = Get-Random $DivisionList

    $LoginID = $Firstname[0] + $Lastname
    $userPrincipalName = $LoginID + $UPNSuffix
    $sAMAccountName = [string]$LoginID[0..19]

    # Define their path in Active Directory
    $ADPath = "OU=$Division,OU=$City,$CompanyRootDN"
    # Create the user in Active Directory
    New-ADUser -Enabled -GivenName $Firstname -Surname $Lastname -DisplayName $Displayname -UserPrincipalName $userPrincipalName -Division $Division -City $City -Path $ADPath -Name $Displayname -SamAccountName $sAMAccountName –UserPassword (Get-CrudePassword)
    # Add User to appropriate Security Group
    $Groupname = (Get-GroupInfo –City $City –Division $Division).Name
    Add-ADGroupmember $Groupname –Members $sAMAccountName
} 

#endregion