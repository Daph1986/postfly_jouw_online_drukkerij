/*
    Core logic/payment flow for this comes from:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from: 
    https://stripe.com/docs/stripe-js
*/


let stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
let client_secret = $('#id_client_secret').text().slice(1, -1);
let stripe = Stripe(stripe_public_key);
let elements = stripe.elements();

let style = {
  base: {
      color: '#000',
      fontFamily: 'Poppins',
      fontSize: '16px',
      '::placeholder': {
          color: '#70707086'
      }
  },
  invalid: {
      color: '#dc3545',
      iconColor: '#dc3545'
  }
};
let card = elements.create('card', {style: style});
card.mount('#card-element');