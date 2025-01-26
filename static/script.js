document.addEventListener('DOMContentLoaded', () => {
    fetch('/data')
        .then(response => response.json())
        .then(data => {
            // Populate currency table
            const currencyTable = document.querySelector('#currency-table tbody');
            for (const [currency, rate] of Object.entries(data.currency_rates)) {
                const row = `<tr><td>${currency}</td><td>${rate}</td></tr>`;
                currencyTable.innerHTML += row;
            }

            // Display gold price
            document.querySelector('#gold-price').textContent = `1 ounce: $${data.gold_price}`;
        })
        .catch(error => console.error('Error fetching data:', error));
});

