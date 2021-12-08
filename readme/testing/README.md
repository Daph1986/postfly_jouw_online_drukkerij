:open_file_folder: Table of Contents
======

**<details><summary>Manual testing</summary>**
* [**_User stories_**](#user-stories)
</details>

**<details><summary>Code check</summary>**
* [**_HTML_**](#html)
* [**_CSS_**](#css)
* [**_JavaScript_**](#javascript)
* [**_Python_**](#python)
* [**_Lighthouse_**](#lighthouse)
* [**_GTmetrix_**](#gtmetrix)
* [**_Color blindness_**](#color-blindness)
* [**_Accessibility_**](#accessibility)
* [**_Travis testing_**](#travis-testing)
* [**_Other tests_**](#other-tests)
</details>

**<details><summary>Bugs</summary>**
* [**_Webhook_**](#webhook)
* [**_Duplicate order_**](#duplicate-order)
* [**_Pagination_**](#pagination)
* [**_Custom order number_**](#custom-order-number)
* [**_Error pages_**](#error-pages)
* [**_Travis form test_**](#travis-form-test)
</details>

:construction_worker_woman: :construction_worker_man: Manual testing
======

### User stories

The design goal is to make a clear, accessible, structured site so that visitors can easily order their printed matter. Below is an overview of the user stories. <br>
<img src="../general/img/user_stories.png" alt="User stories" width="100%" height="100%"><br>

To test the goals screen records of a OnePlus Nord were made.<br>
NOTE: the grey overlay in some captions on the footer are displayed because the end of the screen was captured, when just looking on the device this is not visible. So, this is just the screen records issue of the phone not a site issue!!!<br>
On small devices the menu can be accessed through the hamburger menu, on large devices the navbar is visible at the top. There is a difference between the menu for a user who is not logged in and a user who is logged in.<br>

<img src="../testing/img/loged_out.jpg" alt="Loged out user" width="25%" height="25%"> <img src="../testing/img/loged_in.jpg" alt="Loged in user" width="25%" height="25%"><br>

### Testing the visitor goals
As a shopper / site user I want to be able to:<br>
**<details><summary>#1 see a clear overview of the possibilities /  which products can I order</summary>**

In the menu navigate to `Products`, search for the desirered product in the search bar or on the homepage press the `SHOP NOW` button.<br>
<img src="../testing/img/products_1.jpg" alt="How to find products 1" width="25%" height="25%"> <img src="../testing/img/products_3.jpg" alt="How to find products 3" width="25%" height="25%"> <img src="../testing/img/products_2.jpg" alt="How to find products 2" width="25%" height="25%">
</details>

**<details><summary>#2 see in advance what the costs of the products will be and when it can be delivered</summary>**

On the products page each product is displayed in a card, the price ex VAT is diplayed and the delivery time you choose yourself, either 3 or 5 business days.<br>
<img src="../testing/img/products_4.jpg" alt="Products explained 1" width="25%" height="25%"> <img src="../testing/img/products_5.jpg" alt="Products explained 2" width="25%" height="25%">
</details>

**<details><summary>#3 ask questions if something is not clear</summary>**

Navigate to `Contact / Contact us` in the menu and fill out the contact form.<br>

<img src="../testing/img/contact_1.jpg" alt="Contact explained 1" width="25%" height="25%"> <img src="../testing/img/contact_2.jpg" alt="Contact explained 2" width="25%" height="25%"><br>
<img src="../testing/img/contact_3.jpg" alt="Contact explained 3" width="25%" height="25%"> <img src="../testing/img/contact_4.jpg" alt="Contact explained 4" width="25%" height="25%">
<div align="right"><a href="#top">🔝</a></div>
</details>

**<details><summary>#4 ask for an quotation if a product is not on the site, but maybe in the collection</summary>**

Navigate to `Contact / Quotation request` in the menu and fill out the form.<br>

<img src="../testing/img/contact_5.jpg" alt="Contact explained 5" width="25%" height="25%"> <img src="../testing/img/contact_6.jpg" alt="Contact explained 6" width="25%" height="25%"><br>
<img src="../testing/img/contact_7.jpg" alt="Contact explained 7" width="25%" height="25%"> <img src="../testing/img/contact_8.jpg" alt="Contact explained 8" width="25%" height="25%">
<div align="right"><a href="#top">🔝</a></div>
</details>

**<details><summary>#5 see the different kinds of paper</summary>**

Navigate to `Contact / Free sample kit` in the menu and fill out the form.<br>

<img src="../testing/img/contact_9.jpg" alt="Contact explained 9" width="25%" height="25%"> <img src="../testing/img/contact_10.jpg" alt="Contact explained 10" width="25%" height="25%"><br>
<img src="../testing/img/contact_11.jpg" alt="Contact explained 11" width="25%" height="25%"> <img src="../testing/img/contact_12.jpg" alt="Contact explained 12" width="25%" height="25%">
<div align="right"><a href="#top">🔝</a></div>
</details>

**<details><summary>#6 register an account</summary>**

Navigate to `Register` in the menu and fill out the form and follow the steps.

<img src="../testing/img/register_1.jpg" alt="Registration explained 1" width="25%" height="25%"> <img src="../testing/img/register_2.jpg" alt="Registration explained 2" width="25%" height="25%"> <img src="../testing/img/register_3.jpg" alt="Registration explained 3" width="25%" height="25%"><br>
<img src="../testing/img/register_4.jpg" alt="Registration explained 4" width="25%" height="25%"> <img src="../testing/img/register_5.jpg" alt="Registration explained 5" width="25%" height="25%"> <img src="../testing/img/register_6.jpg" alt="Registration explained 6" width="25%" height="25%">
<div align="right"><a href="#top">🔝</a></div>
</details>

**<details><summary>#7 log in on my account</summary>**

Navigate to `Log in` in the menu<br>

<img src="../testing/img/login_1.jpg" alt="Log in explained 1" width="25%" height="25%"> <img src="../testing/img/login_2.jpg" alt="Log in explained 2" width="25%" height="25%"> <img src="../testing/img/login_3.jpg" alt="Log in explained 3" width="25%" height="25%">
</details>

**<details><summary>#8 recover the password of my account</summary>**

Navigate to `Log in` in the menu and press `Forgot your password?` fill out the form and follow the steps.<br>

<img src="../testing/img/reset_1.jpg" alt="Reset password explained 1" width="25%" height="25%"> <img src="../testing/img/reset_2.jpg" alt="Reset password explained 2" width="25%" height="25%"> <img src="../testing/img/reset_3.jpg" alt="Reset password explained 3" width="25%" height="25%"><br>
<img src="../testing/img/reset_4.jpg" alt="Reset password explained 4" width="25%" height="25%"> <img src="../testing/img/reset_5.jpg" alt="Reset password explained 5" width="25%" height="25%">
<div align="right"><a href="#top">🔝</a></div>
</details>

**<details><summary>#9 see a secured overview of my order history</summary>**

Navigate to `Account / Dashboard` in the menu.<br>

<img src="../testing/img/dashboard_1.jpg" alt="Order history 1" width="25%" height="25%"> <img src="../testing/img/dashboard_2.jpg" alt="Order history 2" width="25%" height="25%"> <img src="../testing/img/dashboard_3.jpg" alt="Order history 3" width="25%" height="25%">
<div align="right"><a href="#top">🔝</a></div>
</details>

**<details><summary>#10 change my details if needed</summary>**

Navigate to `Account / Profile` in the menu.<br>

<img src="../testing/img/profile_1.jpg" alt="Profile 1" width="25%" height="25%"> <img src="../testing/img/profile_1.jpg" alt="Profile 1" width="25%" height="25%"> <img src="../testing/img/profile_1.jpg" alt="Profile 1" width="25%" height="25%">
</details>

**<details><summary>#11 sort products by name, category and price</summary>**

On the homepage press the `SHOP NOW` button, in the menu navigate to `Products` or search for the desirered product in the search bar, and click the sort bar.<br>

<img src="../testing/img/sort_1.jpg" alt="Sorting 1" width="25%" height="25%"> <img src="../testing/img/sort_2.jpg" alt="Sorting 2" width="25%" height="25%">
<div align="right"><a href="#top">🔝</a></div>
</details>

**<details><summary>#12 search a product by name or size (within the sku the size and quantity are mentioned, by using sku searching on size is possible)</summary>**

In the menu navigate search for the desirered product in the search bar, you can search for size, papertype or category.<br>

<img src="../testing/img/search_1.jpg" alt="Searching 1" width="25%" height="25%"> <img src="../testing/img/search_2.jpg" alt="Searching 2" width="25%" height="25%"><br>
<img src="../testing/img/search_3.jpg" alt="Searching 3" width="25%" height="25%"> <img src="../testing/img/search_4.jpg" alt="Searching 4" width="25%" height="25%"><br>
<img src="../testing/img/search_5.jpg" alt="Searching 5" width="25%" height="25%"> <img src="../testing/img/search_6.jpg" alt="Searching 6" width="25%" height="25%">
<div align="right"><a href="#top">🔝</a></div>
</details>

**<details><summary>#13 go through the ordering process in a simple way + #14 to upload my own artwork + #15 have easy acces to my cart, and to be able to delete products that are in the cart, as long as the order isn't put through yet</summary>**

Place the products that you want to order in your cart. Navigate to the `shopping cart` in the menu. As long as you didn't pay you are still able to adjust the cart. Go to `Secure checkout` when you are ready, fill out the checkout form where you can also upload your artwork.

<img src="../testing/img/ordering_1.jpg" alt="How to order 1" width="25%" height="25%"> <img src="../testing/img/ordering_2.jpg" alt="How to order 2" width="25%" height="25%"> <img src="../testing/img/ordering_3.jpg" alt="How to order 3" width="25%" height="25%"><br>
<img src="../testing/img/ordering_4.jpg" alt="How to order 4" width="25%" height="25%"> <img src="../testing/img/ordering_5.jpg" alt="How to order 5" width="25%" height="25%"><br>
<img src="../testing/img/ordering_6.jpg" alt="How to order 6" width="25%" height="25%"> <img src="../testing/img/ordering_7.jpg" alt="How to order 7" width="25%" height="25%">
<div align="right"><a href="#top">🔝</a></div>
</details>

**<details><summary>#13 go through the ordering process in a simple way + #14 to upload my own artwork + #15 have easy acces to my cart, and to be able to delete products that are in the cart, as long as the order isn't put through yet</summary>**

Place the products that you want to order in your cart. Als long as you didn't pay you are still able to adjust the cart. Go to `Secure checkout` when you are ready, fill out the checkout form where you can also upload your artwork.

<img src="../testing/img/ordering_1.jpg" alt="How to order 1" width="25%" height="25%"> <img src="../testing/img/ordering_2.jpg" alt="How to order 2" width="25%" height="25%"> <img src="../testing/img/ordering_3.jpg" alt="How to order 3" width="25%" height="25%"><br>
<img src="../testing/img/ordering_4.jpg" alt="How to order 4" width="25%" height="25%"> <img src="../testing/img/ordering_5.jpg" alt="How to order 5" width="25%" height="25%"><br>
<img src="../testing/img/ordering_6.jpg" alt="How to order 6" width="25%" height="25%"> <img src="../testing/img/ordering_7.jpg" alt="How to order 7" width="25%" height="25%">
<div align="right"><a href="#top">🔝</a></div>
</details>

**<details><summary>#16 receive a clear order confirmation with a description of what I ordered</summary>**

After completing the checkout form and pressing `Complete order` you will get a confirmation by email.<br>
<img src="../testing/img/ordering_8.jpg" alt="How to order 8" width="25%" height="25%"> <img src="../testing/img/ordering_9.jpg" alt="How to order 9" width="25%" height="25%"> <img src="../testing/img/ordering_10.jpg" alt="How to order 10" width="25%" height="25%">
<div align="right"><a href="#top">🔝</a></div>
</details>


### Testing the site owner goals:
As a site owner I want to be able to:<br>
**<details><summary>#17 see a clear overview of the order placed by the customer</summary>**

Make sure you use the admin details to log in, navigate to `Account / Dashboard` in the menu, you will see all the placed orders and can also see the details.<br>
<img src="../testing/img/admin_dashboard.jpg" alt="Admin dashboard" width="25%" height="25%"> <img src="../testing/img/admin_order_detail.jpg" alt="Order detail" width="25%" height="25%">
</details>

**<details><summary>#18 add, updated or delete products on the site</summary>**

Make sure you use the admin details to log in, navigate to `Account / Product management` there you can add a product. If you navigate to `Products` in the menu, you can update and delete a product. <br>
<img src="../testing/img/crud_1.jpg" alt="Navigate to Product management" width="25%" height="25%"> <img src="../testing/img/crud_2.jpg" alt="Product management" width="25%" height="25%"> <img src="../testing/img/crud_3.jpg" alt="Add product" width="25%" height="25%"><br>
<img src="../testing/img/crud_4.jpg" alt="Product added" width="25%" height="25%"> <img src="../testing/img/crud_5.jpg" alt="Product found in search" width="25%" height="25%"> <img src="../testing/img/crud_6.jpg" alt="Update or delete product" width="25%" height="25%"><br>
<img src="../testing/img/crud_7.jpg" alt="Product updated" width="25%" height="25%"> <img src="../testing/img/crud_8.jpg" alt="Updated product found in search" width="25%" height="25%"> <img src="../testing/img/warning.jpg" alt="Warning" width="25%" height="25%"><br>
<img src="../testing/img/crud_9.jpg" alt="Product deleted" width="25%" height="25%"> <img src="../testing/img/crud_10.jpg" alt="Product not found in search" width="25%" height="25%">
<div align="right"><a href="#top">🔝</a></div>
</details>

**<details><summary>#19 be able to download the artwork that was uploaded</summary>**

Log in to the [Django admin panel](https://postfly-jouw-online-drukkerij.herokuapp.com/admin/login/?next=/admin/) with the admin details, navigate to orders and find the artwork at the bottom.<br>
<img src="../testing/img/order_django_admin.jpg" alt="Order in Django admin panel" width="25%" height="25%"> <img src="../testing/img/uploaded_artwork.jpg" alt="Uploaded artwork" width="25%" height="25%">
<div align="right"><a href="#top">🔝</a></div>
</details>
<br>
It can be concluded that all goals have been achieved.<br><br>

The project has been tested on the available DevTools for phone and tablet sizes as well as on multiple responsive sizes and it was made sure that it looks good and works well on all. It was also tested on multiple devices among others a OnePlus Nord, an iMac (Retina 5K, 27-inch, 2017), a MacBook-Air (Retina M1, 13.3-inch, 2020) and a Samsung Galaxy Tab4 (10.1-inch 2014), everything works as it should.
<div align="right"><a href="#top">🔝</a></div>

![HTML5](https://img.shields.io/badge/HTML5%20-%23E34F26.svg?&style=for-the-badge&logo=HTML5&logoColor=FFFFFF)
======

### HTML

The HTML code of the pages was tested with a [HTML](https://validator.w3.org/#validate_by_uri) validator. For a few pages the links are below, but all pages have been checked and no errors or warnings were found.<br>
<img src="../testing/img/html_check.png" alt="Html check" width="55%" height="55%"> <br>

[Home page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpostfly-jouw-online-drukkerij.herokuapp.com%2F)<br>
[Products page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpostfly-jouw-online-drukkerij.herokuapp.com%2Fproducts%2F)<br>
[Specifications page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpostfly-jouw-online-drukkerij.herokuapp.com%2Fspecifications%2F)<br>
[FAQ page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpostfly-jouw-online-drukkerij.herokuapp.com%2Ffaq%2F)<br>
[Team page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpostfly-jouw-online-drukkerij.herokuapp.com%2Fteam%2F)<br>
[Contact page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpostfly-jouw-online-drukkerij.herokuapp.com%2Fcontact%2F)<br>
[Register page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpostfly-jouw-online-drukkerij.herokuapp.com%2Faccounts%2Fsignup%2F)<br>
[Log in page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpostfly-jouw-online-drukkerij.herokuapp.com%2Faccounts%2Flogin%2F)<br>
[Shopping cart](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpostfly-jouw-online-drukkerij.herokuapp.com%2Fcart%2F)<br>
[Dashboard](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpostfly-jouw-online-drukkerij.herokuapp.com%2Fprofile%2F)<br>
[Add product page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpostfly-jouw-online-drukkerij.herokuapp.com%2Fproducts%2Fadd%2F)<br>
[Profile page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpostfly-jouw-online-drukkerij.herokuapp.com%2Fprofile%2Fuser_profile)<br>
[Checkout page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpostfly-jouw-online-drukkerij.herokuapp.com%2Fcheckout%2F)<br>
[Checkout success page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpostfly-jouw-online-drukkerij.herokuapp.com%2Fcheckout%2Fcheckout_success%2F93F585)<br>
[Order detail page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpostfly-jouw-online-drukkerij.herokuapp.com%2Fprofile%2Forder_detail%2F93F585)<br>
<div align="right"><a href="#top">🔝</a></div>

![CSS3](https://img.shields.io/badge/CSS3%20-%231572B6.svg?&style=for-the-badge&logo=CSS3&logoColor=FFFFFF)
======

### CSS

The CSS code was tested with a [CSS](https://jigsaw.w3.org/css-validator/validator.html.en#validate_by_input) validator. <br>
base.css<br>
<img src="../testing/img/css_base_1.png" alt="CSS check base 1" width="55%" height="55%"> <img src="../testing/img/css_base_2.png" alt="CSS check base 2" width="55%" height="55%"> <img src="../testing/img/css_base_3.png" alt="CSS check base 3" width="55%" height="55%"><br>
<div align="right"><a href="#top">🔝</a></div>
checkout.css<br>
<img src="../testing/img/css_checkout_1.png" alt="CSS check checkout 1" width="55%" height="55%"> <img src="../testing/img/css_checkout_2.png" alt="CSS check checkout 2" width="55%" height="55%"><br>
profile.css<br>
<div align="right"><a href="#top">🔝</a></div>
<img src="../testing/img/css_profile_1.png" alt="CSS check profile 1" width="55%" height="50%"> <img src="../testing/img/css_profile_2.png" alt="CSS check profile 2" width="55%" height="55%"><br>

Only warnings were found, but nothing that needs to be fixed or effects the code in a wrong way.
<div align="right"><a href="#top">🔝</a></div>

![JavaScript](https://img.shields.io/badge/JavaScript%20-%23323330.svg?&style=for-the-badge&logo=JavaScript&logoColor=F7DF1E)
======

### JavaScript

The JavaScript code was tested with a [JavaScript](https://jshint.com/) linter. <br>
main.js<br>
<img src="../testing/img/main.png" alt="Main.js check" width="55%" height="55%"><br>
products.js<br>
<img src="../testing/img/products.png" alt="Products.js check" width="55%" height="55%"><br>
toasts.js<br>
<img src="../testing/img/toasts.png" alt="Toasts.js check" width="55%" height="55%"><br>
<div align="right"><a href="#top">🔝</a></div>
stripe_elements.js<br>
<img src="../testing/img/stripe_elements.png" alt="Stripe_elements.js check" width="55%" height="55%"><br>
countryfield.js<br>
<img src="../testing/img/countryfield.png" alt="Countryfield.js check" width="55%" height="55%"><br>
cart.html script<br>
<img src="../testing/img/cart.png" alt="Cart.html script check" width="55%" height="55%"><br>

Only warnings were found, but nothing that needs to be fixed or effects the code in a wrong way.
<div align="right"><a href="#top">🔝</a></div>

![PYTHON](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
======

### Python

The Python code was tested with a [PEP8](http://pep8online.com/) linter. <br>
Below are two examples, the first one is of the checkout app models and the second one is of the checkout app views.<br>
<img src="../testing/img/checkout_models.png" alt="PEP8 checkout models" width="55%" height="55%"><br>
<img src="../testing/img/checkout_views.png" alt="PEP8 checkout views" width="55%" height="55%"><br>
All other python files have also been checked, no errors or warnings were found.

<div align="right"><a href="#top">🔝</a></div>

:traffic_light: Lighthouse
======

### Lighthouse

All pages have passed through Lighthouse in Chrome DevTools, the results can be found here: <br>
### Home page
#### Desktop
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/home_desktop.png" alt="Lighthouse results" width="50%" height="50%">
</details>

#### Mobile
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/home_mobile.png" alt="Lighthouse results" width="50%" height="50%">
</details>

### All products page
#### Desktop
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/products_desktop.png" alt="Lighthouse results" width="50%" height="50%">
</details>

#### Mobile
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/products_mobile.png" alt="Lighthouse results" width="50%" height="50%">
</details>

### Flyers 300 gr mat page
#### Desktop
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/flyers_300_mat_desktop.png" alt="Lighthouse results" width="50%" height="50%">
</details>

#### Mobile
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/flyers_300_mat_mobile.png" alt="Lighthouse results" width="50%" height="50%">
</details>
<div align="right"><a href="#top">🔝</a></div>

### Flyers 300 gr mat A6 page
#### Desktop
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/flyers_300_mat_a6_desktop.png" alt="Lighthouse results" width="50%" height="50%">
</details>

#### Mobile
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/flyers_300_mat_a6_mobile.png" alt="Lighthouse results" width="50%" height="50%">
</details>
The results for the other single pages, other sizes and paper types, is similar, they have been tested but are not shown here because the list would then become too long.

### Specification page
#### Desktop
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/specifications_desktop.png" alt="Lighthouse results" width="50%" height="50%">
</details>

#### Mobile
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/specifications_mobile.png" alt="Lighthouse results" width="50%" height="50%">
</details>

### Templates page
#### Desktop
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/templates_desktop.png" alt="Lighthouse results" width="50%" height="50%">
</details>

#### Mobile
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/templates_mobile.png" alt="Lighthouse results" width="50%" height="50%">
</details>
The results for the other single pages, other sizes and paper types, is similar, they have been tested but are not shown here because the list would then become too long.
<div align="right"><a href="#top">🔝</a></div>

### FAQ page
#### Desktop
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/faq_desktop.png" alt="Lighthouse results" width="50%" height="50%">
</details>

#### Mobile
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/faq_mobile.png" alt="Lighthouse results" width="50%" height="50%">
</details>

### Our team page
#### Desktop
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/team_desktop.png" alt="Lighthouse results" width="50%" height="50%">
</details>

#### Mobile
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/team_mobile.png" alt="Lighthouse results" width="50%" height="50%">
</details>


### Printing in-house page
#### Desktop
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/printing_house_desktop.png" alt="Lighthouse results" width="50%" height="50%">
</details>

#### Mobile
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/printing_house_mobile.png" alt="Lighthouse results" width="50%" height="50%">
</details>
<div align="right"><a href="#top">🔝</a></div>

### Our concept page
#### Desktop
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/concept_desktop.png" alt="Lighthouse results" width="50%" height="50%">
</details>

#### Mobile
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/concept_mobile.png" alt="Lighthouse results" width="50%" height="50%">
</details>

### Contact us page
#### Desktop
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/contact_desktop.png" alt="Lighthouse results" width="50%" height="50%">
</details>

#### Mobile
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/contact_mobile.png" alt="Lighthouse results" width="50%" height="50%">
</details>

### Free sample kit page
#### Desktop
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/sample_desktop.png" alt="Lighthouse results" width="50%" height="50%">
</details>

#### Mobile
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/sample_mobile.png" alt="Lighthouse results" width="50%" height="50%">
</details>
<div align="right"><a href="#top">🔝</a></div>

### Quotation request page
#### Desktop
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/quotation_desktop.png" alt="Lighthouse results" width="50%" height="50%">
</details>

#### Mobile
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/quotation_mobile.png" alt="Lighthouse results" width="50%" height="50%">
</details>

### Register page
#### Desktop
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/register_desktop.png" alt="Lighthouse results" width="50%" height="50%">
</details>

#### Mobile
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/register_mobile.png" alt="Lighthouse results" width="50%" height="50%">
</details>

### Log in page
#### Desktop
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/login_desktop.png" alt="Lighthouse results" width="50%" height="50%">
</details>

#### Mobile
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/login_mobile.png" alt="Lighthouse results" width="50%" height="50%">
</details>
<div align="right"><a href="#top">🔝</a></div>

### Reset password page
#### Desktop
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/reset_desktop.png" alt="Lighthouse results" width="50%" height="50%">
</details>

#### Mobile
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/reset_mobile.png" alt="Lighthouse results" width="50%" height="50%">
</details>

### Shopping cart page
#### Desktop
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/cart_desktop.png" alt="Lighthouse results" width="50%" height="50%">
</details>

#### Mobile
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/cart_mobile.png" alt="Lighthouse results" width="50%" height="50%">
</details>

### Checkout page
#### Desktop
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/checkout_desktop.png" alt="Lighthouse results" width="50%" height="50%">
</details>

#### Mobile
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/checkout_mobile.png" alt="Lighthouse results" width="50%" height="50%">
</details>
<div align="right"><a href="#top">🔝</a></div>

### Checkout success page
#### Desktop
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/checkout_success_desktop.png" alt="Lighthouse results" width="50%" height="50%">
</details>

#### Mobile
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/checkout_success_mobile.png" alt="Lighthouse results" width="50%" height="50%">
</details>

### Dashboard page
#### Desktop
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/dashboard_desktop.png" alt="Lighthouse results" width="50%" height="50%">
</details>

#### Mobile
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/dashboard_mobile.png" alt="Lighthouse results" width="50%" height="50%">
</details>

### Order detail page
#### Desktop
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/order_detail_desktop.png" alt="Lighthouse results" width="50%" height="50%">
</details>

#### Mobile
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/order_detail_mobile.png" alt="Lighthouse results" width="50%" height="50%">
</details>
<div align="right"><a href="#top">🔝</a></div>

### Add product page
#### Desktop
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/add_desktop.png" alt="Lighthouse results" width="50%" height="50%">
</details>

#### Mobile
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/add_mobile.png" alt="Lighthouse results" width="50%" height="50%">
</details>

### Profile page
#### Desktop
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/profile_desktop.png" alt="Lighthouse results" width="50%" height="50%">
</details>

#### Mobile
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/profile_mobile.png" alt="Lighthouse results" width="50%" height="50%">
</details>

### Log out page
#### Desktop
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/logout_desktop.png" alt="Lighthouse results" width="50%" height="50%">
</details>

#### Mobile
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/logout_mobile.png" alt="Lighthouse results" width="50%" height="50%">
</details>

The results of the Lighthouse tests are satisfactory, so no adjustments are needed at this time. But in the future a way to increase the performance and accessibility on some pages would be something to do in an update.

<div align="right"><a href="#top">🔝</a></div>

:bar_chart: GTmetrix
====== 

### GTmetrix

The site was tested with [GTmetrix](https://gtmetrix.com/). The reports of a few pages can be found here:<br>
[Home page](https://gtmetrix.com/reports/postfly-jouw-online-drukkerij.herokuapp.com/HVIpHpjQ/) <br>
[Business cards 400 gr mat 85x55mm page](https://gtmetrix.com/reports/postfly-jouw-online-drukkerij.herokuapp.com/Yng7F52i/) <br>
[Business cards Cold Foil page](https://gtmetrix.com/reports/postfly-jouw-online-drukkerij.herokuapp.com/QSnqI8jh/) <br>
[File type page](https://gtmetrix.com/reports/postfly-jouw-online-drukkerij.herokuapp.com/GCiVdTmp/) <br>
[Job options page](https://gtmetrix.com/reports/postfly-jouw-online-drukkerij.herokuapp.com/xQaop4BH/) <br>
[Overprint page](https://gtmetrix.com/reports/postfly-jouw-online-drukkerij.herokuapp.com/dwBBoi5S/) <br>
GTmetrix also uses Lighthouse, so the reports are similar to the Lighthouse tests.
<div align="right"><a href="#top">🔝</a></div>

:eyeglasses: Color blindness
======

### Color blindness

Color blindness was tested on this [site](https://www.toptal.com/designers/colorfilter/) to ensure you would still be able to read the website when you have different types of color blindness. Here you will find the links of the home page tests, but of course all pages were tested. <br>
[Protanopia](https://www.toptal.com/designers/colorfilter?orig_uri=https://postfly-jouw-online-drukkerij.herokuapp.com/&process_type=protan) <br>
[Deutanopia](https://www.toptal.com/designers/colorfilter?orig_uri=https://postfly-jouw-online-drukkerij.herokuapp.com/&process_type=deutan) <br>
[Tritanopia](https://www.toptal.com/designers/colorfilter?orig_uri=https://postfly-jouw-online-drukkerij.herokuapp.com/&process_type=tritan) <br>
[Greyscale / Achromatopsia](https://www.toptal.com/designers/colorfilter?orig_uri=https://postfly-jouw-online-drukkerij.herokuapp.com/&process_type=grey)

<div align="right"><a href="#top">🔝</a></div>

:heavy_check_mark: Accessibility
======

### Accessibility

Several pages of the site have been tested on accessibility for people with disabilities through the
[Web Accessibility site](https://www.webaccessibility.com/), below are some of the results:
### Home page
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/home.png" alt="Web Accessibility results" width="50%" height="50%">
</details>

### Products page
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/products_acces.png" alt="Web Accessibility results" width="50%" height="50%">
</details>

### Foil page
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/foil.png" alt="Web Accessibility results" width="50%" height="50%">
</details>

### Quotation request page
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/quotation.png" alt="Web Accessibility results" width="50%" height="50%">
</details>

### Register page
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/register.png" alt="Web Accessibility results" width="50%" height="50%">
</details>

### Log in page
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/login.png" alt="Web Accessibility results" width="50%" height="50%">
</details>

### Shopping cart page
<details>
  <summary>Click to see results</summary>
  <img src="../testing/img/cart_access.png" alt="Web Accessibility results" width="50%" height="50%">
</details>

<div align="right"><a href="#top">🔝</a></div>

:mag: Travis testing
======

### Travis testing

The plan was to extensively test with [Travis CI](https://www.travis-ci.com/), but due to time constraints, it has been decided to only check the build and the required fields of the contact, free sample kit and quotation request forms.

### Build history
<details>
  <summary>Click to see build history</summary>
  <img src="../testing/img/travis_1.png" alt="Travis build history" width="50%" height="50%"><br>
  <img src="../testing/img/travis_2.png" alt="Travis build history" width="50%" height="50%"><br>
  <img src="../testing/img/travis_3.png" alt="Travis build history" width="50%" height="50%"><br>
  <img src="../testing/img/travis_4.png" alt="Travis build history" width="50%" height="50%">
</details>

<div align="right"><a href="#top">🔝</a></div>

:test_tube: Other tests
======

### Other tests

A lot of different people were asked to check the project to ensure it works on different systems and devices. The website was tested on Samsung Galaxy TabA (10.1-inch 2019), OnePlus 5, Xiaomi Redmi Note 7, Xiaomi Redmi Note 8 Pro, Motorola G9, Motorola edge 20 lite and iPhone 12 Pro Max among others. It has been tested on the following browsers: Google Chrome, Safari, Microsoft Edge and Mozilla Firefox. During the testing only some misalignments were found. These have been fixed. And a lack of defensive programming was found, for deleting a product, there was no extra warning, so a modal was inserted to check if the admin is sure that the product needs to be deleted.
<br>
The contact forms have been tested on Google Chrome and Safari, they work as they should.<br>
<img src="../testing/img/contact_form_test.png" alt="Travis build history" width="50%" height="50%"><br>
<img src="../testing/img/sample_form_test.png" alt="Travis build history" width="50%" height="50%">
<img src="../testing/img/quotation_form_test.png" alt="Travis build history" width="50%" height="50%">

<div align="right"><a href="#top">🔝</a></div>

:bug: Bugs
======

The bugs are listed below, with a link to the issue item where they are further explained. I was able to solve all of them.

### Webhook
[Stripe webhook payment_intent.succeeded 500 error bug](https://github.com/Daph1986/postfly_jouw_online_drukkerij/issues/10)

### Duplicate order
[Duplicate order bug](https://github.com/Daph1986/postfly_jouw_online_drukkerij/issues/9)

### Pagination
[Pagination bug](https://github.com/Daph1986/postfly_jouw_online_drukkerij/issues/11)

### Custom order number
[Custom order number bug](https://github.com/Daph1986/postfly_jouw_online_drukkerij/issues/14)

### Error pages
[Make error pages bug](https://github.com/Daph1986/postfly_jouw_online_drukkerij/issues/17)

### Travis form test
[Travis form test bug](https://github.com/Daph1986/postfly_jouw_online_drukkerij/issues/24)

<div align="right"><a href="#top">🔝</a></div>
