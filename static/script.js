

function livros_concluidos(){
    console.log("ROdei")
    const livros = document.querySelectorAll("#livros");
    for (const livro of livros) {
        let checkbox = livro.firstElementChild;
        // console.log(checkbox)
        if (checkbox.checked) {
            console.log(livro.textContent, "marcado")

        }
        break

    }
    
}

document.addEventListener("DOMContentLoaded", (event) => {
    livros_concluidos()
})

console.log("Rodei de novo")
livros_concluidos()