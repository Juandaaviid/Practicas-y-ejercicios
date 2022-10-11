function Tabla(){
    let numero=3;
    let table=document.getElementById('tabla');
    for(let i = 1; i<=10; i++){
        let tr = document.createElement('tr');
        tr.id = 'filas';
        tr.className = 'btn-primary';
        tr.innerHTML = '<td>' + numero + 'x' + i + '</td>' + '<td><button class="btn btn-danger">' + numero*i + '</button></td>';
        table.append(tr);

    }
}
Tabla();

function Contenido(){
    let cont= document.getElementById('cont');
    let img=['img1.png','img2.png','img3.png','img4.png']
    for(let i=1; i<=4; i++){
        let div=document.createElement('div');
        div.id='con'+1;
        div.className='col';
        div.innerHTML='<div class="card" style="width: 18rem;">'+
        '<img height="250" src="./img/'+img[i-1]+'" class="card-img-top" alt="...">'+
        '<div class="card-body">'+
        '<h5 class="card-title">Imagen '+ [i]+'</h5>'+
        '<p class="card-text">Some quick example text to build on the card title and make up the bulk of the cards content.</p>'+
        '<a href="#" class="btn btn-primary">Go</a>'+
        '</div>'+
        '</div>';
        cont.append(div);
    }
}
Contenido();