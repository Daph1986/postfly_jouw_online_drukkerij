// ----------------------- Deleting a product from the shopping bag -----------------------
$('.delete-product').click(function(e) {
  let csrfToken = "{{ csrf_token }}";
  let itemId = $(this).attr('id').split('remove_')[1];
  let url = `/bag/remove/${itemId}/`;
  let data = {'csrfmiddlewaretoken': csrfToken};

  $.post(url, data)
    .done(function() {
      location.reload();
    });
});