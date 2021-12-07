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

SCREENSHOTS!!!!

#### Testing the visitor goals
As a shopper / site user I want to be able to:<br>
**<details><summary>#1 see a clear overview of the possibilities /  which products can I order</summary>**
In the menu navigate to `Products`, search for the desirered product in the search bar or on the homepage press the `SHOP NOW` button.<br>
<img src="../testing/img/products_1.jpg" alt="How to find products 1" width="25%" height="25%"> <img src="../testing/img/products_3.jpg" alt="How to find products 3" width="25%" height="25%"> <img src="../testing/img/products_2.jpg" alt="How to find products 2" width="25%" height="25%">
<div align="right"><a href="#top">🔝</a></div>
</details>

**<details><summary>#2 see in advance what the costs of the products will be and when it can be delivered</summary>**
On the products page each product is displayed in a card, the price ex VAT is diplayed and the delivery time you choose yourself, either 3 or 5 business days.
<img src="../testing/img/products_4.jpg" alt="Products explained 1" width="25%" height="25%"> <img src="../testing/img/products_5.jpg" alt="Products explained 2" width="25%" height="25%">
<div align="right"><a href="#top">🔝</a></div>
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
<div align="right"><a href="#top">🔝</a></div>
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
<div align="right"><a href="#top">🔝</a></div>
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

#### The site owners goals are:

<!-- - To share the love for Japanese home cooking and promote it.<br>
The love for Japanese home cooking is explained on the about page, to read it navigate to `About`.
<img src="../testing/testing_images/extended_screen_record_about_page.png" alt="About page" width="25%" height="25%">

<div align="right"><a href="#top">🔝</a></div>

- Share nice Japanese home cooking recipes.<br>
This is shown through the recipes page where all the shared recipes can be found. Navigate to `Recipes` to read them.<br>
<img src="../testing/testing_images/extended_screen_record_recipes_page_1.png" alt="Recipes page 1" width="25%" height="25%"> <img src="../testing/testing_images/extended_screen_record_recipes_page_2.png" alt="Recipes page 2" width="25%" height="25%"> <br><br>

It can be concluded that all goals have been achieved. <br>

The project has been tested on the available DevTools for phone and tablet sizes as well as on multiple responsive sizes and it was made sure that it looks good and works well on all. It was also tested on multiple devices among others a OnePlus Nord, an iMac (Retina 5K, 27-inch, 2017), a MacBook-Air (Retina M1, 13.3-inch, 2020) and a Samsung Galaxy Tab4 (10.1-inch 2014), everything works as it should. -->

<div align="right"><a href="#top">🔝</a></div>

![HTML5](https://img.shields.io/badge/HTML5%20-%23E34F26.svg?&style=for-the-badge&logo=HTML5&logoColor=FFFFFF)
======
### HTML

<!-- The HTML code of all pages was tested with a [HTML](https://validator.w3.org/nu/?doc=http%3A%2F%2Fmamamaki.herokuapp.com%2F) validator.<br>
<img src="../testing/testing_images/html_check_homepage.png" alt="HTML check homepage" width="55%" height="55%"> <br>
<img src="../testing/testing_images/html_check_about_page.png" alt="HTML check about page" width="55%" height="55%"> <br>
<img src="../testing/testing_images/html_check_recipes_page.png" alt="HTML check recipes page" width="55%" height="55%"> <br>
<img src="../testing/testing_images/html_check_personal_recipe_page.png" alt="HTML check personal recipe page" width="55%" height="55%"> <br>
<img src="../testing/testing_images/html_check_add_recipe_page.png" alt="HTML check add recipe page" width="55%" height="55%"> <br>
<img src="../testing/testing_images/html_check_update_recipe_page.png" alt="HTML check edit recipe page" width="55%" height="55%"> <br>
<img src="../testing/testing_images/html_check_log_in_page.png" alt="HTML check log in page" width="55%" height="55%"> <br>
<img src="../testing/testing_images/html_check_register_page.png" alt="HTML check register page" width="55%" height="55%"> <br>
No errors or warnings were found. -->

<div align="right"><a href="#top">🔝</a></div>

![CSS3](https://img.shields.io/badge/CSS3%20-%231572B6.svg?&style=for-the-badge&logo=CSS3&logoColor=FFFFFF)
======

### CSS

<!-- The CSS code was tested with a [CSS](https://jigsaw.w3.org/css-validator/validator.html.en#validate_by_input) validator. <br>
<img src="../testing/testing_images/css_check_1.png" alt="CSS check" width="55%" height="55%"> <img src="../testing/testing_images/css_check_2.png" alt="CSS check" width="55%" height="55%"> <br>

Only warnings were found, but nothing that needs to be fixed or effects the code in a wrong way. -->

<div align="right"><a href="#top">🔝</a></div>

![JavaScript](https://img.shields.io/badge/JavaScript%20-%23323330.svg?&style=for-the-badge&logo=JavaScript&logoColor=F7DF1E)
======

### JavaScript

<!-- The JavaScript code was tested with a [JavaScript](https://jshint.com/) linter. <br>
<img src="../testing/testing_images/js_check_1.png" alt="JS check 1" width="45%" height="45%">
<img src="../testing/testing_images/js_check_2.png" alt="JS check 2" width="45%" height="45%"><br>

Only warnings were found, but nothing that needs to be fixed or effects the code in a wrong way. -->

<div align="right"><a href="#top">🔝</a></div>

![PYTHON](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
======

### Python

<!-- The Python code was tested with a [PEP8](http://pep8online.com/) linter. <br>
<img src="../testing/testing_images/python_check.png" alt="Python check" width="55%" height="55%"><br>
No errors or warnings were found. -->

<div align="right"><a href="#top">🔝</a></div>

:traffic_light: Lighthouse
======

### Lighthouse

<!-- All pages have passed through Lighthouse in Chrome DevTools, the results for desktop can found here: <br>
<img src="../testing/testing_images/home_desktop.png" alt="Lighthouse desktop home" width="25%" height="25%"> <img src="../testing/testing_images/about_desktop.png" alt="Lighthouse desktop about" width="25%" height="25%"> <img src="../testing/testing_images/recipes_desktop.png" alt="Lighthouse desktop recipes" width="25%" height="25%"> <img src="../testing/testing_images/register_desktop.png" alt="Lighthouse desktop register" width="25%" height="25%"> <img src="../testing/testing_images/log_in_desktop.png" alt="Lighthouse desktop log in" width="25%" height="25%"> <img src="../testing/testing_images/personal_recipe_page_desktop.png" alt="Lighthouse desktop personal recipe page" width="25%" height="25%"> <img src="../testing/testing_images/add_recipe_desktop.png" alt="Lighthouse desktop add recipe" width="25%" height="25%"> <img src="../testing/testing_images/edit_recipe_desktop.png" alt="Lighthouse desktop edit recipe" width="25%" height="25%"><br>
and these are the results for the mobile versions:<br>
<img src="../testing/testing_images/home_mobile.png" alt="Lighthouse mobile home" width="25%" height="25%"> <img src="../testing/testing_images/about_mobile.png" alt="Lighthouse mobile about" width="25%" height="25%"> <img src="../testing/testing_images/recipes_mobile.png" alt="Lighthouse mobile recipes" width="25%" height="25%"> <img src="../testing/testing_images/register_mobile.png" alt="Lighthouse mobile register" width="25%" height="25%"> <img src="../testing/testing_images/login_mobile.png" alt="Lighthouse mobile log in" width="25%" height="25%"> <img src="../testing/testing_images/personal_recipe_page_mobile.png" alt="Lighthouse mobile personal recipe page" width="25%" height="25%"> <img src="../testing/testing_images/add_recipe_mobile.png" alt="Lighthouse mobile add recipe" width="25%" height="25%"> <img src="../testing/testing_images/edit_recipe_mobile.png" alt="Lighthouse mobile edit recipe" width="25%" height="25%"><br>
The results of the Lighthouse tests are satisfactory, so no adjustments are needed at this time. But in the future a way to increase the performance on some pages would be something to do in an update. -->

<div align="right"><a href="#top">🔝</a></div>

:bar_chart: GTmetrix
====== 

### GTmetrix

<!-- The site was tested with [GTmetrix](https://gtmetrix.com/). The reports can be found here:<br>
[Homepage](https://gtmetrix.com/reports/mamamaki.herokuapp.com/DtF79YmN/) <br>
[About page](https://gtmetrix.com/reports/mamamaki.herokuapp.com/ehQW2KTp/) <br>
[Recipes page](https://gtmetrix.com/reports/mamamaki.herokuapp.com/Aok6T3gH/) <br>
[Single recipe page](https://gtmetrix.com/reports/mamamaki.herokuapp.com/FMvG3INv/) <br>
[Register page](https://gtmetrix.com/reports/mamamaki.herokuapp.com/nxjFnBeX/) <br>
[Log in page](https://gtmetrix.com/reports/mamamaki.herokuapp.com/NfTTBCfW/) <br>
[Personal recipe page](https://gtmetrix.com/reports/mamamaki.herokuapp.com/f0CLM9rG/) <br>
[Add recipe](https://gtmetrix.com/reports/mamamaki.herokuapp.com/OZgPHOwf/) <br>
[Edit recipe](https://gtmetrix.com/reports/mamamaki.herokuapp.com/hL6hdl9W/) <br> -->

<div align="right"><a href="#top">🔝</a></div>

:eyeglasses: Color blindness
======

### Color blindness

<!-- Color blindness was tested on this [site](https://www.toptal.com/designers/colorfilter/) to ensure you would still be able to read the website when you have different types of color blindness. Here you will find the links of the homepage tests, but of course all pages were tested. <br>
[Protanopia](https://www.toptal.com/designers/colorfilter?orig_uri=http://mamamaki.herokuapp.com/&process_type=protan) <br>
[Deutanopia](https://www.toptal.com/designers/colorfilter?orig_uri=http://mamamaki.herokuapp.com/&process_type=deutan) <br>
[Tritanopia](https://www.toptal.com/designers/colorfilter?orig_uri=http://mamamaki.herokuapp.com/&process_type=tritan) <br>
[Greyscale / Achromatopsia](https://www.toptal.com/designers/colorfilter?orig_uri=http://mamamaki.herokuapp.com/&process_type=grey) -->

<div align="right"><a href="#top">🔝</a></div>

:test_tube: Other tests
======

### Other tests

<!-- A lot of different people were asked to check the project to ensure it works on different systems and devices. The website was tested on Samsung Galaxy TabA (10.1-inch 2019), OnePlus 5, Xiaomi Redmi Note 7, Xiaomi Redmi Note 8 Pro, Motorola G9, Motorola G5 and iPhone 12 Pro Max among others. It has been tested on the following browsers: Google Chrome, Safari, Microsoft Edge and Mozilla Firefox. During the testing two bugs were found and fixed, the Safari button bug and the Multiple cards in one card bug, please see the Bugs section and matching issue link for these bugs and their fix.
<br>
The contact form of the home page has also been tested on Google Chrome, Safari, Microsoft Edge and Mozilla Firefox, this works as it should.<br>
<img src="../testing/testing_images/emailjs_test.png" alt="EmaiJS test" width="55%" height="55%"> -->

#### Advices given after testing which were followed

<!-- 1. Some spelling and grammar changes have been made after reviews from my husband, brother-in-law and sister-in-law.
2. My husband, Django, did not think the user-friendliness was good enough, because only the logo could be used to return to the homepage. That is why on the page for requesting the sample kit and for designing the business card, 2 buttons have been added at the top to switch between the other pages. Cancel buttons have also been added to the bottom of the forms. This increases user-friendliness. -->

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
