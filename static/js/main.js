
    // Check if geolocation is supported
    if ("geolocation" in navigator) {
      navigator.geolocation.getCurrentPosition(function(position) {
        var latitude = position.coords.latitude;
        var longitude = position.coords.longitude;

        // Create a Geocoder instance
        var geocoder = new google.maps.Geocoder();

        // Define the location based on latitude and longitude
        var latlng = new google.maps.LatLng(latitude, longitude);

        // Perform reverse geocoding
        geocoder.geocode({ 'location': latlng }, function(results, status) {
          if (status === google.maps.GeocoderStatus.OK) {
            if (results[0]) {
              // Display the formatted address
              document.getElementById("location").innerText = "Address: " + results[0].formatted_address;
            } else {
              document.getElementById("location").innerText = "No results found";
            }
          } else {
            document.getElementById("location").innerText = "Geocoder failed due to: " + status;
          }
        });
      });
    } else {
      // Geolocation is not supported
      document.getElementById("location").innerText = "Geolocation is not supported by your browser";
    }


    // scripts for menu
    // script.js
const dropdownBtn = document.querySelectorAll(".dropdown-btn");
const dropdown = document.querySelectorAll(".dropdown");
const hamburgerBtn = document.getElementById("hamburger");
const navMenu = document.querySelector(".menu");
const links = document.querySelectorAll(".dropdown a");

function setAriaExpandedFalse() {
  dropdownBtn.forEach((btn) => btn.setAttribute("aria-expanded", "false"));
}

function closeDropdownMenu() {
  dropdown.forEach((drop) => {
    drop.classList.remove("active");
    drop.addEventListener("click", (e) => e.stopPropagation());
  });
}

function toggleHamburger() {
  navMenu.classList.toggle("show");
}

dropdownBtn.forEach((btn) => {
  btn.addEventListener("click", function (e) {
    const dropdownIndex = e.currentTarget.dataset.dropdown;
    const dropdownElement = document.getElementById(dropdownIndex);

    dropdownElement.classList.toggle("active");
    dropdown.forEach((drop) => {
      if (drop.id !== btn.dataset["dropdown"]) {
        drop.classList.remove("active");
      }
    });
    e.stopPropagation();
    btn.setAttribute(
      "aria-expanded",
      btn.getAttribute("aria-expanded") === "false" ? "true" : "false"
    );
  });
});

// close dropdown menu when the dropdown links are clicked
links.forEach((link) =>
  link.addEventListener("click", () => {
    closeDropdownMenu();
    setAriaExpandedFalse();
    toggleHamburger();
  })
);

// close dropdown menu when you click on the document body
document.documentElement.addEventListener("click", () => {
  closeDropdownMenu();
  setAriaExpandedFalse();
});

// close dropdown when the escape key is pressed
document.addEventListener("keydown", (e) => {
  if (e.key === "Escape") {
    closeDropdownMenu();
    setAriaExpandedFalse();
  }
});

hamburgerBtn.addEventListener("click", toggleHamburger);

// automatic slider
let slideIndex = 0;
showSlides();

function showSlides() {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}
  slides[slideIndex-1].style.display = "block";
  setTimeout(showSlides, 4000); // Change image every 2 seconds
}


// swiper

document.addEventListener("DOMContentLoaded", function () {
  const list = document.getElementById("myList");
  const button = document.getElementById("showMoreBtn");
  const items = list.getElementsByTagName("li");

  let itemsToShow = 21; // Initial number of items to show
  let itemsVisible = itemsToShow;

  // Show the initial set of items
  for (let i = 0; i < itemsVisible; i++) {
      if (items[i]) {
          items[i].classList.add("visible");
      }
  }

  button.addEventListener("click", function () {
      // Calculate how many more items to show
      let newVisibleCount = itemsVisible + itemsToShow;

      // Show additional items
      for (let i = itemsVisible; i < newVisibleCount; i++) {
          if (items[i]) {
              items[i].classList.add("visible");
          }
      }

      itemsVisible = newVisibleCount;

      // If all items are visible, hide the button
      if (itemsVisible >= items.length) {
          button.style.display = "none";
      }
  });
});


