Lists and arrays are the same most of the time BUT

# Create lists
$LISTNAME = "ITEM", "ITEM", "ITEM"

i.e. $ips = "1.1.1.1", "8.8.8.8", "10.10.10.10"

# Use list
foreach($ip in $ips){
  ping $ip
}
## OUTPUT
Pings each Ip

# To add item to list
$LISTNAME += "NEWITEM"

i.e. $ips += "3.3.3.3"


# Visual
foreach($ip in $ips){
  ping $ip
  echo "---------------------------------------------"
}
## OUTPUT
Ping 1st ip
------------------------------------------------
Pings 2nd ip
------------------------------------------------
etc.

# To remove item from list
First change [System.Collection.Arraylist]$LISTNAME = "ITEM", "ITEM", "ITEM"
$LISTNAME = "ITEM"