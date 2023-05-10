// make create acount pop_up
let btn_create = document.querySelector(".create");
btn_create.onclick = function(){
    let popoverlay = document.createElement("div");
            popoverlay.className = "popup-overlay"
            document.body.appendChild(popoverlay)
            // create popupbox

        let popbox = document.createElement("div");
            popbox.className = "pop-box";
            popoverlay.appendChild(popbox);

        let h1 = document.createElement("h1");
        h1txt = document.createTextNode("Sign Up")
        h1.appendChild(h1txt)

        let p = document.createElement("p");
        let txtp = document.createTextNode("It's quick and easy")
        p.appendChild(txtp);

        popbox.appendChild(h1)
        popbox.appendChild(p)
        let hr = document.createElement("hr")
        popbox.appendChild(hr)

        let form = document.createElement("form")
        form.className = "class_box"
        let inputs = document.createElement("div");
        inputs.className = "inputs_div"

        let inputs1 = document.createElement("input")
        inputs1.type = "text";
        inputs1.placeholder = "first name"
        inputs1.className = "fname";
        let inputs2 = document.createElement("input")
        inputs2.type = "text";
        inputs2.placeholder = "surname"
        inputs2.className = "sname";
        let inputs3 = document.createElement("input")
        inputs3.placeholder = "Email"
        inputs3.type = "eamil";
        inputs3.className = "number";
        let inputs4 = document.createElement("input")
        inputs4.type = "password";
        inputs4.placeholder = "New password"
        inputs4.className = "pass";
        
        // make div for brith
        
        let divbrith = document.createElement("div")
        divbrith.className = "divbrith"
        

        let input5 = document.createElement("input");

        input5.type="number"
        input5.placeholder = "dd"
        input5.className = "days";
        let input6 = document.createElement("input");
        input6.type="text"
        input6.placeholder = "mm"
        input6.className = "month";
        let input7 = document.createElement("input");
        input7.type="number"
        input7.placeholder = "yy"
        input7.className = "years";

         // make gender/

        let divg = document.createElement("div")
        divg.id = "divg"
        
        divg.innerHTML =`<div class="gender">
        <p id="para1">what is ur Gender?<p><br>
        <div class="male">
            <label for="male">Male</label>
            <input type="radio" id="male">
        </div>
        <div class="female">
            <label for="female">Female</label>
            <input type="radio" id="female">
        </div>
        <div class="custom">
            <label for="custom">Custom</label>
            <input type="radio" id="custom">
        </div>

    </div>
`
 
let btn = document.createElement("input")
btn.type="submit"
btn.value = "Sign Up"
btn.id = "btn"



let span = document.createElement("span");

span.id = "sp"
spantxt = document.createTextNode("X")
span.appendChild (spantxt);    



        inputs.appendChild(inputs1)
        inputs.appendChild(inputs2)
        inputs.appendChild(inputs3)
        inputs.appendChild(inputs4)
        inputs.appendChild(divbrith)
        divbrith.appendChild(input5)
        divbrith.appendChild(input6)
        divbrith.appendChild(input7)
        inputs.appendChild(divg)

        inputs.appendChild(btn)
   

        popbox.appendChild(span)

        form.appendChild(inputs)
        popbox.appendChild(form)
        // body.appendChild(popoverlay)


        span.onclick = function(){
            
            popoverlay.style.display = "none"
        }


}

