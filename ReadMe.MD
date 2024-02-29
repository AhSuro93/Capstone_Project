<URLs>

<`Web Browser`>
# http://127.0.0.1:8000/ `# Does Not Work`
# http://127.0.0.1:8000/admin/ `# Django Admin Panel`
# http://127.0.0.1:8000/restaurant/ `# Home Page`


<`Menu API`>
# http://127.0.0.1:8000/restaurant/menu/> `# Menu API`
# http://127.0.0.1:8000/restaurant/menu/1 `# Menu API Single Menu Item`


<`Booking Tables API (Authenticated Views)`>
# http://127.0.0.1:8000/restaurant/booking/ `# Tell Available URLs Made By DefaultRouter`
# http://127.0.0.1:8000/restaurant/booking/.json `# API Root In JSON Format`
# http://127.0.0.1:8000/restaurant/booking/tables/ `# Booking List - Made This Route Authenticated Make Sure To Run Migrations Then Use Token`
# http://127.0.0.1:8000/restaurant/booking/tables/1/ `# Booking Single Instance`
# http://127.0.0.1:8000/restaurant/booking/tables.json `# JSON Format`
# http://127.0.0.1:8000/restaurant/booking/tables/1.json `# Booking Single Instance In JSON Format`


`Djoser`
# http://127.0.0.1:8000/auth/ `# Default Basic Root View For DefaultRouter`
# http://127.0.0.1:8000/auth/users/ `# List All Users`
# http://127.0.0.1:8000/auth/token/login/ `# Login Page`
# http://127.0.0.1:8000/auth/token/logout/ `# Logout Page`


<`Insomnia`>
# http://127.0.0.1:8000/restaurant/api-token-auth/ `# Used In Insomnia For Token String`


===================================================================
<Users>

`admin`
{
    "auth_token": "30d4cadac662ff041d8dfe29d3d37b66f5df1b0d"
}

Username: `Adrian` 
Email: adrian@littlelemon.com
Password: lemon@adr!
{
    "auth_token": "ef00acbef1c8807aaa7be2f45c9d9714946d8712"
}


Username:`Mario`
Email: mario@littlelemon.com
Password: lemon@mar!
{
    "auth_token": "e85136aa9c7d46e40de195a27b36bcd6e8c0a917"
}

<No_Token_For_The_Following>
Username: `Sana`
Email: sana@littlelemon.com
Password: lemon@san!


Username: `Emily`
Email: emily@littlelemon.com
Password: lemon@em!
