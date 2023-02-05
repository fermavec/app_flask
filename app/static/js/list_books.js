(function(){
    const btnBuyBook = document.querySelectorAll('.btn-buy-book');
    let isbnSelectedBook = null;
    const csrf_token = document.querySelector("[name='csrf-token']").value;

    btnBuyBook.forEach((btn) => {
        btn.addEventListener('click', function(){
            isbnSelectedBook=this.id;
            confirmPurchase();
        });
    });

    /*Uso de Fetch API*/ 
    const confirmPurchase = async() => {
        await fetch('http://127.0.0.1:5005/buybook', {
        method:'POST',
        mode:'same-origin',
        credentials:'same-origin',
        headers:{
            'Content-Type':'application/json',
            'X-CSRF-TOKEN': csrf_token
        },
        body:JSON.stringify({
            isbn:isbnSelectedBook
        })
        }).then(response => {
            if(!response.ok){
                console.error('Error!');
            }
            return response.json();
        }).then(data => {
            console.log('Book Purchased');
        }).catch(error => {
            console.error(`error: ${error}`);
        });
    };
})();