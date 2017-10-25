# django-agreements
Appliaction allows to show the information in the form of plain text or pdf to the users after login. The information needs to be confirmed by the user before he can proceed further. The agreements could be assigned only to the selected users or to all users.
Application comes with easy to use admin panel

## How to set up
1. Add `agreements` to installed apps
2. Add `agreements.display_agreement_middleware` to the list of middlewares
3. Add `agreements.urls` to the list of urls

## How to use
After set up agreements should appear in your django admin site allowing you to add messages for the users. Just try it out. To change the default layout of the messages overwrite application templates in your own project. 
