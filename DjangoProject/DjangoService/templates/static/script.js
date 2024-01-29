document.addEventListener('DOMContentLoaded', function () {
    var stripe = Stripe('pk_test_51OQer7JOA0Vjtm2XdDA0CYpoGqcioJzGlhwDAUcvFZY0vixjM4ammOh4KHrur1OFtweIQbSfqUnFCXwcI3Ra2Skv00qYoQweyv');
    var buyButton = document.getElementById('buy-button');

    buyButton.addEventListener('click', function () {
        // Replace this with the correct way to get the item ID from your HTML.
        var itemId = parseInt(document.getElementById('item-id').textContent);

        // Fetch the session ID from the backend
        fetch(`/buy/${itemId}`)
            .then(response => response.json())
            .then(session => {
                // Redirect to the Stripe Checkout page
                return stripe.redirectToCheckout({ sessionId: session.session_id });
            })
            .then(result => {
                if (result.error) {
                    alert(result.error.message);
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
    });
});
