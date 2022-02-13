# Burgerzilla Project (Yemeksepeti & Patika.dev Python Web Development Bootcamp Final Project)

![381669388162271](https://user-images.githubusercontent.com/58272864/153778599-3f0b6ee8-ccbe-43c4-a5b4-866eb45d2cd3.png)

This project consists of two separate microservices. One of them, Burgerzilla API, is a REST-API micro-service that takes orders from hamburger restaurants, can view the status of the order, and enables transactions with customer/restaurant authorization regarding the order. The second of them is a microservice called Auth API, which allows restaurants and customers to register and login, and then issue JWT tokens to users.

## Run the project with Docker

    docker-compose up

## Run the test

    flask test
    
## Folder structure
    
    burgerzilla-restapi
     ┣ app
     ┃ ┣ api
     ┃ ┃ ┣ customer
     ┃ ┃ ┃ ┣ controller.py
     ┃ ┃ ┃ ┣ dto.py
     ┃ ┃ ┃ ┣ service.py
     ┃ ┃ ┃ ┣ utils.py
     ┃ ┃ ┃ ┗ __init__.py
     ┃ ┃ ┣ restaurant
     ┃ ┃ ┃ ┣ controller.py
     ┃ ┃ ┃ ┣ dto.py
     ┃ ┃ ┃ ┣ service.py
     ┃ ┃ ┃ ┣ utils.py
     ┃ ┃ ┃ ┗ __init__.py
     ┃ ┃ ┣ authorization_check.py
     ┃ ┃ ┗ __init__.py
     ┃ ┣ auth
     ┃ ┃ ┣ controller.py
     ┃ ┃ ┣ dto.py
     ┃ ┃ ┣ service.py
     ┃ ┃ ┣ utils.py
     ┃ ┃ ┗ __init__.py
     ┃ ┣ models
     ┃ ┃ ┣ orders.py
     ┃ ┃ ┣ products.py
     ┃ ┃ ┣ restaurant.py
     ┃ ┃ ┣ schemas.py
     ┃ ┃ ┣ users.py
     ┃ ┃ ┗ __init__.py
     ┃ ┣ extensions.py
     ┃ ┣ utils.py
     ┃ ┗ __init__.py
     ┣ logs
     ┣ tests
     ┃ ┣ utils
     ┃ ┃ ┣ base.py
     ┃ ┃ ┣ common.py
     ┃ ┃ ┗ __init__.py
     ┃ ┣ test_auth_customer.py
     ┃ ┣ test_auth_restaurant.py
     ┃ ┗ __init__.py
     ┣ .env
     ┣ .gitignore
     ┣ boot.sh
     ┣ config.py
     ┣ docker-compose.yml
     ┣ Dockerfile
     ┣ README.md
     ┣ requirements.txt
     ┗ runburgerzilla.py
## Database Structure
![image](https://user-images.githubusercontent.com/58272864/153779353-1b85f963-4d3e-4975-9935-cd1de8e2e268.png)

# Auth API 

A REST-API micro-service that enables customers and restaurants to login and register. In addition, customers and restaurants receive JWT tokens with this micro-service, which they will use later.

`Postman Documentation` 
    https://documenter.getpostman.com/view/19453056/UVeNm2hn

## Auth Customer (`auth/customer`)

Customers endpoints

### Customer Login

`POST /login`


#### Input Data
    Content-Type: application/json
    {
        "email": "ugurozy@musteri.nett",
        "password": "12345"
    }


### Customer Register

`POST /register`

#### Input Data
    Content-Type: application/json
    {
        "fullname": "Ezel Özyalı",
        "email": "ezelozy@musteri.nett",
        "password": "12345"
    }

## Auth Restaurant (`auth/restaurant`)
Restaurant endpoints

### Restaurant Login

`POST /login`

#### Input Data
    Content-Type: application/json
    {
        "email": "omerk@restaron.net",
        "password": "12345"
    }

### Restaurant Register

`POST /register`

#### Input Data
    Content-Type: application/json

    {
        "fullname": "Tunç Dimdal",
        "email": "tuncd@restaron.net",
        "password": "12345",
        "restaurant_name": "Dublemumble"
    }


# Burgerzilla API
A REST-API micro-service that takes orders from hamburger restaurants, can view the status of the order, and enables transactions with customer/restaurant authorization regarding the order.

`Postman Documentation`
    https://documenter.getpostman.com/view/19453056/UVeNm2ho


## Api Customer (`api/customer`)

Customers endpoints


### Create a new order 

`POST /order/<int:res_id>`

#### Input Data
    Content-Type: application/json

    {
        "product_ids": int,
        "quantities": int
    }


### Get order list

`GET /orderlist`

#### Response Data
    Content-Type: application/json

    {
        "product_ids": List,
        "quantities": List
    }

### Get specific order 

`GET /<int:order_id>`

#### Response Data
    Content-Type: application/json

    {
        'order_id': int
        'user_id': int
        'product_ids': int
        'quantities': int
        'order_date': datetime
        'order_status': int
    }

### Update specific order 

`PUT /<int:order_id>`

#### Input Data
    Content-Type: application/json

    {
        "quantities": int
    }

### Cancel specific order 

`DELETE /<int:order_id>`

#### Response Data
    Content-Type: application/json

    {
        "status": status,
        "message": message
    }




## Api Restaurant (`api/restaurant`)

Restaurant endpoints


### Get specific order

`GET /<int:order_id>`

#### Response Data
    Content-Type: application/json

    {
        'order_id': int
        'res_id': int
        'user_id': int
        'product_ids': int
        'quantities': int
        'order_date': datetime
        'order_status': int
    }


### Update specific order

`Update /<int:order_id>`


### Cancel specific order

`Delete /<int:order_id>`

### Get all orders

`Get /orderlist`

### Get menu

`GET /menu`

#### Response Data
    Content-Type: application/json

    {
        'order_id': int
        'user_id': int
        'product_ids': int
        'quantities': int
        'order_date': datetime
        'order_status': int
    }

### Add product

`POST /menu`

### Get all products

`GEtT /menuProducts`



### Get menu

`GET /menu/<int:product_id>`

#### Response Data
    Content-Type: application/json

    {
        'order_id': int
        'user_id': int
        'product_ids': int
        'quantities': int
        'order_date': datetime
        'order_status': int
    }

### Update specific product

`PUT /menu/<int:product_id>`

### Delete specific product

`DELETE /menu/<int:product_id>`


