function filterList() {
    let input = document.getElementById("search").value.toLowerCase();
    let items = document.querySelectorAll(".card");
    items.forEach(item => {
        if (item.textContent.toLowerCase().includes(input)) {
            item.style.display = "";
        } else {
            item.style.display = "none";
        }
    });
}

async function convert() {
    const amount = document.getElementById("amount").value;
    const currency = document.getElementById("currency").value;
    const response = await fetch(`/currency?amount=${amount}&currency=${currency}`);
    const result = await response.json();
    document.getElementById("result").innerText = `Converted amount: ${result.convertedAmount}`;
}

