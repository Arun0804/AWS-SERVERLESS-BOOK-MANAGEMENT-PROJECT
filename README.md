
#  Serverless Book Management Application on AWS

##  Overview

This is a **serverless web application** that allows users to **insert book records** and **view all stored books**.

The project demonstrates a complete end-to-end **cloud-native architecture** using AWS services, including:

* Static hosting
* Serverless compute
* Managed NoSQL database
* API-based backend
* Secure, scalable deployment

The full stack is built without provisioning or managing servers.

---

##  Features

* Add book details (title, author, year)
* Retrieve all stored books
* Serverless architecture (auto-scalable, low-cost)
* Web-based UI built with HTML/CSS/JavaScript
* REST APIs powered by API Gateway
* Fully managed database (DynamoDB)
* Secure global content delivery via CloudFront

---

##  Architecture

![Architecture Diagram](Architecture.png)

---

##  AWS Services Used

| Service            | Purpose                     |
| ------------------ | --------------------------- |
| Amazon S3          | Hosts static frontend       |
| Amazon CloudFront  | CDN + SSL for global access |
| Amazon API Gateway | Exposes REST API endpoints  |
| AWS Lambda         | Executes GET and POST logic |
| Amazon DynamoDB    | Stores book data            |
| IAM                | Security and access control |
| CloudWatch         | Monitoring and logs         |

---

##  Tech Stack

* HTML, CSS, JavaScript
* jQuery (AJAX requests)
* Python (Lambda)
* AWS Serverless services

---

##  Project Structure

```
.
├── index.html               # UI
├── scripts.js               # AJAX logic
├── insertBookData.py        # Lambda - insert
└── getBooks.py              # Lambda - get all
```

---

## 🔧 APIs

### **POST /books**

Add a book record:

Request format:

```json
{
  "bookid": "optional",
  "title": "Book Title",
  "author": "Author Name",
  "year": "Optional"
}
```

Response:

```json
"Book data saved successfully!"
```

---

### **GET /books**

Returns an array of stored books:

Example response:

```json
[
    {
        "bookid": "123",
        "title": "Book A",
        "author": "Author A",
        "year": "2024"
    }
]
```

---

##  DynamoDB Table

| Attribute | Type   | Description   |
| --------- | ------ | ------------- |
| bookid    | String | Partition key |
| title     | String | Book title    |
| author    | String | Author        |
| year      | String | Optional      |

---

## 🏁 Setup & Deployment

### 1. Create DynamoDB Table

* Name: `bookData`
* PK: `bookid` (String)

### 2. Create Lambda Functions

Upload files:

* `insertBookData.py`
* `getBooks.py`

Set handler as:

```
insertBookData.lambda_handler
getBooks.lambda_handler
```

### 3. Permissions

Give Lambdas access to DynamoDB:

* `PutItem`
* `Scan`
* `Query` (optional)

### 4. Create API Gateway

Resource:

```
/books
```

Methods:

* **POST** → insertBookData
* **GET** → getBooks

Enable CORS.

Deploy API.
Copy endpoint URL.

### 5. Host Frontend on S3

* Enable static website hosting
* Upload:

  * `index.html`
  * `scripts.js`

In `scripts.js`, replace:

```js
var API_ENDPOINT = "YOUR_API_ENDPOINT_HERE";
```

### 6. (Optional) Configure CloudFront

* Origin: S3 bucket
* Behaviors: allow GET, HEAD
* SSL Certificate
* Point DNS to CloudFront

---

##  Benefits of Serverless Architecture

* Zero server maintenance
* Pay-per-use cost model
* Auto scaling
* Highly available
* Fast global performance


---

##  What I Learned

* Designing serverless architectures
* API Gateway + Lambda integration
* NoSQL data modeling with DynamoDB
* IAM least-privilege access
* Debugging production cloud apps
* End-to-end deployment lifecycle


