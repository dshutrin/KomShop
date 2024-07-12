function delete_product(product_id){
    document.getElementById('modal').style.display = 'block';
    document.getElementById('id').innerHTML = product_id;
}

function delet(){
    product_id = document.getElementById('id').innerHTML;
    const xhr = new XMLHttpRequest();
    xhr.open('GET', '/admin_panel/delete_product/' + product_id);
    document.getElementById(product_id).style.display = 'none';
    document.getElementById('modal').style.display = 'none';
    xhr.send();
}

function tag_make_other(tag_id, prod_id){
    var xhr = new XMLHttpRequest();
    xhr.open("POST", '/admin_panel/tag_make_other');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send('tag_id=' + tag_id + '&prod_id' + prod_id);
}

function tag_make_product(tag_id, prod_id){
    var xhr = new XMLHttpRequest();
    xhr.open("POST", '/admin_panel/tag_make_product');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send('tag_id=' + tag_id + '&prod_id' + prod_id);
}

function cat_make_other(cat_id, prod_id){
    var xhr = new XMLHttpRequest();
    xhr.open("POST", '/admin_panel/cat_make_other');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send('cat_id=' + cat_id + '&prod_id' + prod_id);
}

function cat_make_product(cat_id, prod_id){
    var xhr = new XMLHttpRequest();
    xhr.open("POST", '/admin_panel/cat_make_product');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send('cat_id=' + cat_id + '&prod_id' + prod_id);
}