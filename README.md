![Library Gif](http://25.media.tumblr.com/948e64b952b036c0c3d2c7469a2075a8/tumblr_n3kratI12p1t96jpzo1_500.gif)

# BOOKS

### GET ALL BOOKS (GET)

                https://brittanica-books.onrender.com/api/v1/books/

### GET SPECIFIC BOOK BY LOCCCN (GET)
                https://brittanica-books.onrender.com/api/v1/book/?locccn=int


### CREATE NEW BOOK (POST)
                https://brittanica-books.onrender.com/api/v1/users/{user_id}/books


*payload (Example Value)*
```js
{
  "title": "string",
  "locccn": 0
}
```

### UPDATE A BOOK (PUT)
                https://britanncaflask.pythonanywhere.com/api/books/{id}

*payload (Example value)*
```js
{
  "title": "string",
  "locccn": 0
}
```
### DELETE A BOOK
                https://britanncaflask.pythonanywhere.com/api/books/{id} -->

# USERS
### GET ALL USERS (GET)
                https://brittanica-books.onrender.com/api/v1/users

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
