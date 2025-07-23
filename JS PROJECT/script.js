const users = [
  {
    name: "amisha rathore",
    pic: "https://i.pinimg.com/736x/cd/9b/1c/cd9b1cf5b96e8300751f952488d6c002.jpg",
    bio: "silent chaos in a loud world 🌑🖤 | not for everyone",
  },
  {
    name: "kiara mehta",
    pic: "https://i.pinimg.com/736x/1f/2f/85/1f2f856bf3a020ed8ee9ecb3306ae074.jpg",
    bio: "main character energy 🎬 | coffee > everything ☕✨",
  },
  {
    name: "isha oberoi",
    pic: "https://i.pinimg.com/736x/23/48/7e/23487ef1268cfe017047a0640318c0d0.jpg",
    bio: "walking through dreams in doc martens ☁️🖤 | late night thinker",
  },
  {
    name: "Ojin Okwara",
    pic: "https://images.unsplash.com/photo-1732167372202-30be36e1168e?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    bio: "too glam to give a damn 😎 | true free soul",
  },
  {
    name: "diya bansal",
    pic: "https://images.unsplash.com/photo-1607746882042-944635dfe10e",
    bio: "i like cheese a lot 🧀🧡 | i just dooo",
  },
  {
    name: "tanay rawat",
    pic: "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde",
    bio: "don’t blink 🌟 | never change ever",
  },
  {
    name: "mohit chhabra",
    pic: "https://plus.unsplash.com/premium_photo-1750153889748-b031ec974a42?q=80&w=687&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    bio: "aesthetic overload 🎨 | living in lowercase",
  },
];

function clearCards() {
  document.querySelector(".cards").innerHTML = "";
}

function showUsers(arr) {
  const container = document.querySelector(".cards");
  arr.forEach((user) => {
    const card = document.createElement("div");
    card.classList.add("card");

    const img = document.createElement("img");
    img.src = user.pic;
    img.classList.add("bg-img");

    const blurredLayer = document.createElement("div");
    blurredLayer.style.backgroundImage = `url('${user.pic}')`;
    blurredLayer.classList.add("blurred-layer");

    const content = document.createElement("div");
    content.classList.add("content");

    const heading = document.createElement("h3");
    heading.textContent = user.name;

    const paragraph = document.createElement("p");
    paragraph.textContent = user.bio;

    content.appendChild(heading);
    content.appendChild(paragraph);

    card.appendChild(img);
    card.appendChild(blurredLayer);
    card.appendChild(content);

    container.appendChild(card);
  });
}

function NoUserFound() {
  const container = document.createElement("div");
  container.classList.add("not-found");

  const img = document.createElement("img");
  img.src = "https://cdn-icons-png.flaticon.com/512/2748/2748558.png";
  img.alt = "No User";
  img.className = "back-img w-24 h-24 opacity-60";

  const heading = document.createElement("h2");
  heading.textContent = "No User Found";
  heading.className = "text-xl font-semibold text-white mb-1";

  const paragraph = document.createElement("p");
  paragraph.textContent =
    "We couldn’t find any user with that information. Please try again.";
  paragraph.className = "text-white text-center";

  const button = document.createElement("button");
  button.textContent = "Go Back";
  button.className =
    "mt-4 bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition-all";
  button.onclick = () => {
    // alert("Going back...");
    inp.value = "";
    container.remove();
    showUsers(users);
    
  };

  container.appendChild(img);
  container.appendChild(heading);
  container.appendChild(paragraph);
  container.appendChild(button);

  document.querySelector(".cards").appendChild(container);
}

showUsers(users);

const inp = document.querySelector(".inp");

inp.addEventListener("input", function () {
  const newUsers = users.filter((user) =>
    user.name.toLowerCase().startsWith(inp.value.toLowerCase())
  );

  clearCards();

  if (newUsers.length > 0) {
    showUsers(newUsers);
  } else {
    NoUserFound();
  }
});
