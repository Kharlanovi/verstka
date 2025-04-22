async function get_news() {
    let response = await fetch ("http://127.0.0.1:8010/api/news/")
    if (response.ok){
        return response.json();    
    }
}
async function render_news() {
   let container =  document.getElementById("news")
   let news = await get_news()
   news.forEach(item => {
    let template = '<div class="news">'
    + '<h2>{name}</h2>'
    + '<p>{description}</p>'
    + '<span>{date}</span>'
    + '<img src= "{image}">'
    + '<button><img src="../img/disrep.png"></button><span id="rep-{id}">{rep}</span><button><img src="../img/rep.png"></button>'
    + '</div>'
    template = template.replaceAll("{id}", item.id)
    template = template.replaceAll("{name}", item.name)
    template = template.replaceAll("{description}", item.description)
    template = template.replaceAll("{date}", item.date)
    template = template.replaceAll("{image}", item.image)
    template = template.replaceAll("{rep}", item.rep)
 
    container.innerHTML += template;
})
}
render_news();