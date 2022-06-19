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


let button = document.querySelector("#button_for_bye");

button.addEventListener('click', function(){


    const request = new Request(
        "http://127.0.0.1:8000/sole/",
        {
            method: 'POST',
            headers: {'X-CSRFToken': csrftoken},
            mode: 'same-origin', // Do not send CSRF token to another domain.
            body: `{
                "id" : localStorage.getItem("user"),
                "product_id" : localStorage.getItem("product_id"),
                "csrftoken" : csrftoken
            }`
            
        }
    );
    fetch(request).then(function(response) {
        // document.location.href="../";
        console.log(response);
    })
});

