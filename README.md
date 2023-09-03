![Library Gif](http://25.media.tumblr.com/948e64b952b036c0c3d2c7469a2075a8/tumblr_n3kratI12p1t96jpzo1_500.gif)

# BOOKS

### GET ALL BOOKS (GET)

                https://brittanicadjango.pythonanywhere.com/api/v1/books/

### CREATE NEW BOOK (POST)
                https://brittanicadjango.pythonanywhere.com/api/v1/books/


*payload (Example Value)*
```js
{
  "title":"String",
  "user":0,
  "locccn":0,
  "description":"String"
}
```

### UPDATE A BOOK (PUT)
                https://brittanicadjango.pythonanywhere.com/api/v1/books/{book_id}

*payload (Example value)*
```js
{
  "title": "string",
  "locccn": 0,
    "description":"String"  
}
```
### DELETE A BOOK
                https://brittanicadjango.pythonanywhere.com/api/v1/books/{book_id}

# USERS
### GET ALL USERS (GET)
                https://brittanicadjango.pythonanywhere.com/api/v1/users/

### GET SPECIFIC USER (GET)
                https://brittanica-books.onrender.com/api/v1/users{id}

### CREATE NEW USER (POST)
                https://brittanica-books.onrender.com/api/v1/users


*payload (Example Value)*
```js
{
  "email": "string",
  "password":"string"
}
```

### UPDATE A USER (PUT)
            https://brittanica-books.onrender.com/api/v1/users/{id}

*payload (Example value)*
```js
{
  "email": "string",
  "is_active": bool,

}
```

### DELETE A USER (DELETE) 
               https://brittanica-books.onrender.com/api/v1/users/{id}
