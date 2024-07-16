
const header = document.querySelector('header')


const footer = document.querySelector("footer");


header.innerHTML = `

<div class="container">
<a href="/">
<img src="/static/img/logosk8.jpeg" width="170px" class="logo">

</a>
    
<nav>
    <a href="/">Home</a>
    <a href="#nuestros-productos">Nuestros Productos</a>
    <a href="#noticias">GameXtime</a>
    <a href="#mas+"> Mas +</a>  
    
</nav>
 
<div class="search-container">
    <input type="text" placeholder="Buscar..." class="search-box" id="search-box">
    <button type="submit" class="search-button"></button>
    <a href="/login"><img id="C13B8KL" style="width: 26px; height: 26px;" src="/static/img/logg.png" alt="21" width="21" height="21"></a>&nbsp; &nbsp;        

    </div>  

</div> 


`;


footer.innerHTML = `

<section id="mas+">
    <section id="seccion-final">
        <div class="container">
            
            <div class="productos">
                <div class="carta2">
                    <p>LOCALIZACIÓN</p>          
                    <button>
                        <a href="https://www.google.com">Store SK8, Santiago, Metropolitana, Chile</a>
                    </button>
                        
                </div>
                <div class="carta2">
                    <p> REDES SOCIALES</p>
                    <a href="https://www.instagram.com/volcom_inside_chile/"><img id="C13B8KL" style="width: 21px; height: 21px;" src="/static/img/instagram.png" alt="" width="21" height="21"></a>&nbsp; &nbsp; 
                    <a href="https://www.facebook.com/Insideshop"><img style="width: 21px; height: 21px;" src="/static/img/facebook.webp" alt="" width="21" height="21"></a>&nbsp; &nbsp; 
                    <a href="https://twitter.com/volcomlatam?lang=es"><img style="width: 21px; height: 21px;" src="/static/img/Twitter.webp" alt="" width="21" height="21"></a>&nbsp; &nbsp; 
                    <a href="https://ar.pinterest.com/volcom/"><img style="width: 21px; height: 21px;" src="/static/img/Pinterest.webp" alt="" width="21" height="21"></a>&nbsp; &nbsp; 
                    <a href="https://www.youtube.com/channel/UCCMLg_F2RXH1g37rUFN9szg"><img style="width: 21px; height: 21px;" src="/static/img/Youtube.webp" alt="" width="21" height="21"></a> 
                </div>
                <div class="carta2">
                    <p>  AdminiN SK8  </p>                  
                    <nav>              
                        <a href="/accounts/login">Administrador</a>
                        <a href="https://ar.pinterest.com/volcom/">Preguntas frecuentes</a>   
                    </nav>
                </div>

            </div>
        </div>  
    </section>
</section>



<div class="container">
        <img src="/static/img/logosk8.jpeg" width="130px" class="logo">
        <p>SK8, LLC. Todos los derechos reservados</p>
        <iframe style="border: 0;" src="https://cdn.smooch.io/message-us/index.html?channel=whatsapp&amp;color=green&amp;size=compact&amp;radius=20px&amp;label=Contactanos&amp;number=56963064036" 
        width="125" height="30">                
</div>

`;







