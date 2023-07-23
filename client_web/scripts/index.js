BASE_URL = 'http://127.0.0.1:8000/api/v1/'

function get_tasks_request() {
    return fetch(BASE_URL + "tasks/", {
        method: "GET",
        headers: {
            'Content-Type': 'application/json', // Set the appropriate content type if sending JSON data
        }
    }).then(resp => resp.json())
    .then(data => data);
}

function get_task_request(id) {
    return fetch(BASE_URL + `tasks/${id}/`, {
        method: "GET",
        headers: {
            'Content-Type': 'application/json', // Set the appropriate content type if sending JSON data
        }
    }).then(resp => resp.json())
    .then(data => data);
}

function generate_question() {
    return fetch(BASE_URL + `qa/generate/?language=Python`, {
        method: "GET",
        headers: {
            'Content-Type': 'application/json', // Set the appropriate content type if sending JSON data
        }
    }).then(resp => resp.json())
    .then(data => data);
}

function solve_task_request(code) {
    return fetch(BASE_URL + `tasks/${id}/`, {
        mode: 'cors',
        method: "GET",
        headers: {
            'X-CSRFToken': csrftoken
        },
    }).then(resp => resp.json())
    .then(data => data);
}

function get_answer_request(question_id) {
    return fetch(BASE_URL + `qa/${question_id}/answer/`, {
        method: "GET",
        headers: {
            'Content-Type': 'application/json', // Set the appropriate content type if sending JSON data
        }
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
        task_body.className = "card-body"
        task_obj.appendChild(task_body)
        task_title = document.createElement('a')

        var currentUrl = window.location.href;

        // Находим индекс последнего символа "/"
        var lastSlashIndex = currentUrl.lastIndexOf('/');

        // Удаляем все после последнего символа "/"
        var newUrl = currentUrl.substring(0, lastSlashIndex + 1);

        task_title.href = newUrl + `task.html?id=${task.id}`
        task_title2 = document.createElement('h1')
        task_title2.appendChild(document.createTextNode(task.title))
        task_title.append(task_title2)
        task_description = document.createElement('p')
        task_description.appendChild(document.createTextNode(task.description))
        task_body.appendChild(task_title)
        task_body.appendChild(task_description)  
        tasks_obj.appendChild(task_obj) 
    });
    
}

async function fill_info() {
    const urlParams = new URLSearchParams(window.location.search);
    const task_id = urlParams.get('id'); 
    task = await get_task_request(task_id)
    title = document.getElementById("title")
    title.appendChild(document.createTextNode(task.title))
    description = document.getElementById("description")
    description.appendChild(document.createTextNode(task.title))
    content = document.getElementById("content")
    content.appendChild(document.createTextNode(task.description))
}

async function get_question() {
    question_paragraph = document.getElementById("question")
    question_paragraph.appendChild(document.createTextNode(" Загрузка..."))
    question = await generate_question()
    question_paragraph.innerHTML = ""
    question_paragraph.appendChild(document.createTextNode(question.title))
    answer_button = document.getElementById("answer_button")
    answer_button.style.visibility = "visible"
    localStorage.setItem("question", question.id)
    answer_paragraph = document.getElementById("answer")
    answer_paragraph.innerHTML = ""
}

async function get_answer() {
    question_id = localStorage.getItem("question")
    answer_paragraph = document.getElementById("answer")
    answer_paragraph.innerHTML = ""
    answer = await get_answer_request(question_id)
    answer_paragraph.appendChild(document.createTextNode(answer.title))
}