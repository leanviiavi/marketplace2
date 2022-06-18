function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');
console.log(csrftoken);


let bue = document.querySelectorAll(".button_bue");

let indexOfProduct = 0;

bue.forEach(element => {
    element.addEventListener('click', function(){
        let form = document.createElement("form");
        form.setAttribute("method", "POST");
        form.setAttribute("action", "/current/");

        let id = document.createElement("input");
        id.name = "id"; id.setAttribute("value", indexOfProduct);

        let user_id = document.createElement("input");
        let u_id = localStorage.getItem("user");
        user_id.name = "user_id"; user_id.setAttribute("value", u_id);
        form.appendChild(id);
        form.appendChild(user_id);
        let csrf = document.createElement("input");
        csrf.style.display = "none";
        csrf.type = "hidden";
        csrf.name = "csrfmiddlewaretoken";
        csrf.value = csrftoken;
        form.appendChild(csrf);
        document.body.append(form);
        form.submit();

        
        // location.href = "/current/";
    })
});
