function toCelsius(){

	// grabs the input from the user
	let input =  document.getElementById("temperature").value;
    

	// converts the temperature to C
	let celsius = (input - 32) * 5/9;
    if (isNaN(celsius)) {
        document.getElementById("result-parent").innerText = "Please input a valid number!";
        document.getElementById("result-parent").style.color = "red";
        document.getElementById("result-parent").style.fontWeight = "bold";
        document.getElementById("result-parent").style.visibility = "visible";

    }
    else {
        document.getElementById("result-parent").innerText = "Temperature in Celsius is " + celsius + ".";
        document.getElementById("result-parent").style.color = "black";
        document.getElementById("result-parent").style.fontWeight = "normal";
        document.getElementById("result-parent").style.visibility = "visible";
    }

	
}