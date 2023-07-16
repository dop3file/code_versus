BASE_URL = 'http://127.0.0.1:8000/api/v1/'
const csrftoken = Cookies.get('csrftoken');

function get_tasks_request() {
    return fetch(BASE_URL + "tasks/", {
        mode: 'cors',
        method: "GET",
        headers: {
            'X-CSRFToken': csrftoken
            },
    }).then(resp => resp.json())
    .then(data => data);
}

async function spawn_tasks() {
    tasks = await get_tasks_request()
    tasks_obj = document.getElementById("tasks")
    tasks["results"].forEach(task => {
        var task_obj = document.createElement('div')
        task_obj.className = "card"
        task_body = document.createElement('div')
        task_obj.appendChild(task_body)
        task_title = document.createElement('h1')
        task_title.appendChild(document.createTextNode(task.title))
        task_description = document.createElement('p')
        task_description.appendChild(document.createTextNode(task.description))
        task_body.appendChild(task_title)
        task_body.appendChild(task_description)  
        tasks_obj.appendChild(task_obj) 
    });
    
}

spawn_tasks()