function goBack() {
    console.log('button click')
    location.href = './home.html';
}

function expand(which_one) {
    if (which_one === 1) {
        description = document.createElement("p");
        description.innerText = "The story follows a spy who has to \"build a family\" to execute a mission, not realizing that the girl he adopts as his daughter is a telepath, and the woman he agrees to be in a marriage with is a skilled assassin. ";
        description.style.color = "magenta";
        description.style.fontWeight = "bold";
        description.style.visibility = "visible";
        document.getElementById("spyfam").appendChild(description);
        document.getElementById("spyfam").getElementsByClassName("moreInfo")[0].style.visibility = "hidden";
    }
    if (which_one === 2) {
        description = document.createElement("p");
        description.innerText = "In the senior high school division of Shuchiin Academy, student council president Miyuki Shirogane and vice president Kaguya Shinomiya appear to be a perfect match. Kaguya is the daughter of a wealthy conglomerate family, and Miyuki is the top student at the school and well-known across the prefecture. Although they like each other, they are too proud to confess their love, as they believe whoever does so first would lose. The story follows their many schemes to make the other one confess or at least show signs of affection.";
        description.style.color = "magenta";
        description.style.fontWeight = "bold";
        description.style.visibility = "visible";
        document.getElementById("kaguya").appendChild(description);
        document.getElementById("kaguya").getElementsByClassName("moreInfo")[0].style.visibility = "hidden";
    }

    if (which_one === 3) {
        description = document.createElement("p");
        description.innerText = "Demon Slayer: Kimetsu no Yaiba (\"Blade of Demon Destruction\") is a Japanese manga series written and illustrated by Koyoharu Gotouge. It follows teenage Tanjiro Kamado, who strives to become a demon slayer after his family was slaughtered and his younger sister, Nezuko, turned into a demon.";
        description.style.color = "magenta";
        description.style.fontWeight = "bold";
        description.style.visibility = "visible";
        document.getElementById("demonslayer").appendChild(description);
        document.getElementById("demonslayer").getElementsByClassName("moreInfo")[0].style.visibility = "hidden";
    }

    


    
}