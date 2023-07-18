// function togglePopup(){
//     document.getElementById("popup-1").classList.toggle("active");
// }
// function togglePopup(){
//     document.getElementById("popup-2").classList.toggle("active");
// }
// function togglePopup(){
//     document.getElementById("popup-3").classList.toggle("active");
// }
// function togglePopup(){
//     document.getElementById("popup-4").classList.toggle("active");
// }
// function togglePopup(){
//     document.getElementById("popup-5").classList.toggle("active");
// }


let ids=["popup-1","popup-2","popup-3","popup-4","popup-5"];
function togglePopup(ids){
        for(let i=0;i<=ids.length;i++){
            const id=ids[i];
            document.getElementById(id).classList.toggle("active");
        }
}


//Add to favorites
// // Get references to the elements
// const addToFavoritesButtons = document.querySelectorAll('.add-to-favorites');
// const favoritesList = document.getElementById('favorites-list');

// // Array to store added cards
// const addedCards = [];

// // Add click event listeners to each "Add to Favorites" button
// addToFavoritesButtons.forEach(button => {
//     button.addEventListener('click', addToFavorites);
// });

// // Function to handle adding a card to favorites
// function addToFavorites(event) {
//     const card = event.target.parentNode;

//     // Check if the card is already added
//     if (addedCards.includes(card)) {
//         return; // Exit the function if the card is already added
//     }

//     const cardClone = card.cloneNode(true);

//     // Create a remove button for the cloned card
//     const removeButton = document.createElement('button');
//     removeButton.classList.add('remove-from-favorites');
//     removeButton.textContent = 'Remove from Favorites';
//     removeButton.addEventListener('click', removeFromFavorites);

//     // Hide the "Add to Favorites" button in the cloned card
//     const addToFavoritesButton = cardClone.querySelector('.add-to-favorites');
//     addToFavoritesButton.style.display = 'none';

//     // Append the remove button to the cloned card
//     cardClone.classList.add('favorite-card');
//     cardClone.appendChild(removeButton);

//     // Add the cloned card to the favorites list
//     favoritesList.appendChild(cardClone);

//     // Add the card to the added cards array
//     addedCards.push(card);
// }

// // Function to handle removing a card from favorites
// function removeFromFavorites(event) {
//     const card = event.target.parentNode;
//     card.parentNode.removeChild(card);
//     // Remove the card from the added cards array
//     const index = addedCards.indexOf(card);
//     if (index > -1) {
//         addedCards.splice(index, 1);
//     }

//     // Reload the page after removing the car
//     location.reload();
// }

// script.js
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
