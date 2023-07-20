let ids=["popup-1","popup-2","popup-3","popup-4","popup-5"];
function togglePopup(ids){
        for(let i=0;i<=ids.length;i++){
            const id=ids[i];
            document.getElementById(id).classList.toggle("active");
        }
}

// search function
const searchInput = document.getElementById('searchInput');
const cardContainer = document.querySelector('.card-container');
const cards = cardContainer.querySelectorAll('.content');

function displayCards(filteredCards) {
    cards.forEach((card) => {
        const title = card.getAttribute('data-title').toLowerCase();
        if (filteredCards.includes(title)) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
}

function filterCards(searchTerm) {
    const filteredCards = Array.from(cards)
        .map((card) => card.getAttribute('data-title').toLowerCase())
        .filter((title) => title.includes(searchTerm));

    displayCards(filteredCards);
}

searchInput.addEventListener('input', (event) => {
    const searchTerm = event.target.value.toLowerCase();
    filterCards(searchTerm);
});



// Function called when the filter is changed
function filterCreatures() {
    const selectedFilter = document.getElementById('filter').value;
    const cards = document.querySelectorAll('.content');

    cards.forEach(card => {
        if (selectedFilter === 'all' || card.classList.contains(selectedFilter)) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
}

// Initially show all creatures
filterCreatures();
