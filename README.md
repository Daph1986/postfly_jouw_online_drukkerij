POSTFLY 
Jouw online drukkerij!
======

**[Code Institute](https://codeinstitute.net/)  Milestone Project 4: Full Stack Frameworks with Django**

<img src="readme/general/logo.png" alt="Logo" width="75%" height="75%">

POSTFLY is a site where you can order all your necessary printed matter online.
[POSTFLY](http://www.postfly.nl/) already has an existing site, but it needs an update.
The existing site as it is now no longer meets the needs of customers and employees. This is a first draft for the company's new site and in this case is for educational purposes only.

The focus with this site is to combine knowledge about everything conserning printed matter with what was learned during the Code Institute course.
The site's goal is to have a more efficient system for employees and a easy to understand order system for B2B customers.

:clapper: Demo
======

<!-- By clicking this [link]() a live demo version will be visible. -->

<!-- <img src="static/readme_images/mockup_1.png" alt="Mockup 1" width="65%" height="65%">
<img src="static/readme_images/mockup_2.png" alt="Mockup 2" width="65%" height="65%"> -->
<div align="right"><a href="#top">🔝</a></div>

:open_file_folder: Table of Contents
======

**<details><summary>UX</summary>**
* [**_User stories_**](#user-stories)
    * [_Strategy_](#strategy)
    * [_Scope_](#scope)
    * [_Structure_](#structure)
    * [_Skeleton_](#skeleton)
</details>

**<details><summary>Features</summary>**
* [**_Existing Features_**](#existing-features)
* [**_Features for the future_**](#features-for-the-future)
</details>

**<details><summary>Technologies</summary>**
* [**_Languages_**](#languages)
* [**_Libraries and frameworks_**](#libraries-and-frameworks)
* [**_Wireframes_**](#wireframes)
* [**_Tools_**](#tools)
</details>

**<details><summary>Testing and Bugs</summary>**
* [**_Testing file_**](#testing-file)
</details>

**<details><summary>Deployment</summary>**
* [**_Deployment_**](#deployment)
</details>

**<details><summary>Credits</summary>**
* [**_Content_**](#content)
* [**_Code_**](#code)
* [**_Media_**](#media)
* [**_Other_**](#other)
* [**_Acknowledgements_**](#acknowledgements)
</details>
<br>
<div align="right"><a href="#top">🔝</a></div>

:busts_in_silhouette: UX
======

This is meant to be a B2B site which targets visitors who are in need of printed matter, such as flyers, folders, posters, business cards, brochures, etc.

### User stories

##### User Goals

- As a user I want to see a clear overview of the possibilities, what can I order. (All products page / Menu -> products)
- As a user I want to see in advance what the costs will be and when it can be delivered. (Product page)
- As a user I want to be able to ask questions if something is not clear. (Contact form)
- As a user I want to be able to ask for a quotation if a product is not on the site, but maybe in the collection. (Quatation form)
- As a user I want to be able to see the different kinds of paper. (Sample kit form)
- As a user I want to be able to go through the ordering process in a simple way. (Shopping bag / Checkout)
- As a user I want to be able to upload my own artwork. (Checkout)
- As a user I want to have easy acces to my cart, and to be able to delete products that are in the cart, as long as the order isn't put through yet. (Shopping cart)
- As a user I want to receive a clear order confirmation with a description of what I ordered. (Confirmation email)
- As a user I want to be able to see a secured overview of my order history. (Dashboard)
- As a user I want to have my details filled out in advance, but also be able to change them if needed. (Profile)
- As a user I want to be able to choose the language. (Dutch or English)

##### Site Owners Goals

- As an employee I want to be able to see a clear overview of the order placed by the customer. (Admin dashboard / Admin order details)
- As an employee I want to be able to change the status of an order (Admin order details)
- As an employee I want to be able to updated or delete products of the site. (Admin)
- As an employee I want to be able to download the artwork that was uploaded. (Admin order details)

### Strategy

The design goal is to make a clear, accessible, structured site so that visitors can easily order their printed matter.

### Scope

For customers, the site should be an improvement over the existing site. Frequently heard complaints with the existing site include that it is not clear where the artwork should be uploaded and that the payment system is not working.
If this can be done, it will also ease the workload of the employees, by solving many complaints and questions related to the site.

### Structure

The site will be structured as clear as possible, with a logic workflow and it should be easy to navigate the site on all screen sizes. 

### Skeleton

The skeleton section is a bit more extensive, for that reason please view this separate [file](readme/skeleton/README.md).

### Fonts and icons

[Google Fonts](https://fonts.google.com/) was used to embed the Poppins font in the code. Poppins was chosen because this has a good readability and fits the company's identity.
[FFONTS](https://www.ffonts.net/Syntha-Regular.font.download) was used to get the Syntha Regular font for the subtext of the logo.
For the icons [Font Awesome](https://fontawesome.com/) was used.
<div align="right"><a href="#top">🔝</a></div>

:star2: Features
======

### Existing Features

The site contains the following features: 
- A page with an overview of all the products which can be sort by name, price and category.
- A product detail page with the prices of the products and the delivery times.
- A frequently asked questions page.
- Pages with tips and tricks about designing / handing in artwork.
- A contact form where customers can ask questions.
- A form where customers can request a quote or deviating products / products that are not on the site but we may have.
- A sample kit form where customers can request a sample kit with our paper types.
- A register page.
- A login page.
- A page for when the customer forgot their password.
- An order sytem, to order the products and upload the artwork for the products.
- A dashboard, with the order history.
- A profile page to adjust the user's details. 
- An option to choose the language, Dutch or English. Default will be Dutch.

### Features for the future 

The following features can be added: 

- Integrate the previously created project POSTFLY Business card creator into this site, so that customers can create their design on the site instead of uploading their separately made artwork.
- A chat function for live chat with an employee.
- An artwork upload system where you as a customer can check the artwork theirself.
- An option to have multiple billing and delivery addresses for one user.
<div align="right"><a href="#top">🔝</a></div>

:gear: Technologies
======

### Languages

- HTML
- CSS
- Python
- JavaScript

### Libraries and Frameworks

- Bootstrap
- Postgres
- Stripe
- Pillow
- Boto3
- Django
- Django-allauth
- Django-crispy-forms 
- Django-countries


### Wireframes

- [Adobe XD](https://www.adobe.com/products/xd.html)

### Tools

- [Adobe Photoshop](https://www.adobe.com/products/photoshop.html): to resize the images.
- [Adobe Illustrator](https://www.adobe.com/products/illustrator.html): to create the logo.
- [VSCode](https://code.visualstudio.com/): to write the code in.
- [Heroku](https://www.heroku.com/): as a host for the deployed site.
- [GitHub](https://github.com/): for the repository.
<div align="right"><a href="#top">🔝</a></div>

:test_tube: :bug: Testing and Bugs 
======

### Testing file

<!-- The tests have been done on multiple devices and browsers. In the end everything works as intended. Because this topic contained more content than expected, a separate page was created.
For more details about testing and bugs please view this [file](testing/README.md). -->
<div align="right"><a href="#top">🔝</a></div>

:computer: Deployment
======

### Deployment

<!-- The deployment section is a bit more extensive for that reason please view this separate [file](deployment/README.md). -->
<div align="right"><a href="#top">🔝</a></div>

:copyright: Credits
======

### Content
Most content has been written by me, the prices and technical stories regarding the delivery of the files and the origin of the printing house come from the sites of [POSTFLY](http://www.postfly.nl/) and [Grafische Groep Matthys](https://www.groepmatthys.com/) and were sometimes adjusted by me.

### Code


<div align="right"><a href="#top">🔝</a></div>

### Media

#### Images

1. [POSTFLY](http://www.postfly.nl/) the POSTFLY logo provided by my colleague Filip Matthys.
2. [Flaticon](https://www.flaticon.com/free-icon/paper-plane_164627?term=paper%20plane&page=3&position=52&page=3&position=52&related_id=164627&origin=search) to get and adjust the paper plane of the logo.
3. [favicon.io](https://favicon.io/favicon-converter/) was used to get the favicon of the logo.
4. [Color-hex](https://www.color-hex.com/) was used to get the images of the colors that were used.
5. [Grafische Groep Matthys](https://www.groepmatthys.com/) for their logo,  the images of the foil samples, the head office and the presses, thanks for my colleague Bart Lauwaert for providing the original photos to me.

### Other

1. [Luchidchart](https://www.lucidchart.com/pages/) to create the Django diagram model.
1. [Tinypng](https://tinypng.com/) to resize the wireframe png's.

<!-- 3. [cdnjs](https://cdnjs.com/) to get the fontawesome cdn from.
5. [Am I Responsive?](http://ami.responsivedesign.is/) to check the responsiveness and make the mockups.
6. [WebAIM](https://webaim.org/resources/contrastchecker/) used for checking contrasts on the site. -->

### Acknowledgements

- My mentor from Code Institute, thank you Narender for your time and guidance.
- My husband, thank you Django for taking more care of our son so I can work on my education, and thank you for your patience.
<!-- - Special thanks to my colleagues, friends and family for their support, tips and for testing my project. -->
<div align="right"><a href="#top">🔝</a></div>