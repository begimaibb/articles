// async function buttonClick(event){
//     let target = event.target;
//     let url = target.dataset.articleLink;
//     console.log(url);
//     let response = await fetch(url);
//     let articles_json = await response.json()
//     articles_json.
//     console.log(articles_json)
//     console.log(articles_json.test)
// }
//
//
// function getArticles(){
//     let button = document.getElementById("button");
//     button.addEventListener("click", buttonClick)
// }
//
// window.addEventListener("load", getArticles)

let likeCount = document.querySelector('#likeCount');
let dislikeCount = document.querySelector('#dislikeCount');

function count(){
  likeCount.value = parseInt(likeCount.value) + 1;
}

function dislike(){
  dislikeCount.value = parseInt(dislikeCount.value) + 1;
}