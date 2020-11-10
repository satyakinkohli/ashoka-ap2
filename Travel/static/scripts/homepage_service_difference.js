    document.body.style.backgroundRepeat = "no-repeat";
    document.body.style.backgroundPosition = "center center";
    document.body.style.backgroundAttachment = "fixed";
    document.body.style.backgroundSize = "100% 100%";
    // document.body.style.backgroundSize = "1440px 822.5px";

    document.getElementById("flights_search_bar").style.display = "none";
    document.getElementById("hotels_search_bar").style.display = "none";
    document.getElementById("cabs_search_bar").style.display = "none";

    window.onload = function hotel_outlook() {
        document.body.style.backgroundImage = "url('https://upload.wikimedia.org/wikipedia/commons/0/09/Mumbai_Aug_2018_%2843397784544%29.jpg')";
        document.getElementById("hotels_search_bar").style.display = "block";
    }

    function hotel_outlook() {
        document.body.style.backgroundImage = "url('https://upload.wikimedia.org/wikipedia/commons/0/09/Mumbai_Aug_2018_%2843397784544%29.jpg')";
        var x = document.getElementById("hotels_search_bar");
        document.getElementById("flights_search_bar").style.display = "none";
        document.getElementById("cabs_search_bar").style.display = "none";
        if (x.style.display === "none") {
            x.style.display = "block";
        }
    }

    function flight_outlook() {
        document.body.style.backgroundImage = "url('https://singularityhub.com/wp-content/uploads/2018/12/airplane-flying-above-clouds_shutterstock_553131187-1068x601.jpg')";
        var x = document.getElementById("flights_search_bar");
        document.getElementById("hotels_search_bar").style.display = "none";
        document.getElementById("cabs_search_bar").style.display = "none";
        if (x.style.display === "none") {
            x.style.display = "block";
        }
    }

    function cab_outlook() {
        document.body.style.backgroundImage = "url('https://img.etimg.com/thumb/width-1200,height-900,imgsize-673077,resizemode-1,msid-72892426/news/economy/policy/taxi-policy-guidelines-cab-surge-pricing-could-be-capped-at-thrice-the-base-fare.jpg')";
        var x = document.getElementById("cabs_search_bar");
        document.getElementById("hotels_search_bar").style.display = "none";
        document.getElementById("flights_search_bar").style.display = "none";
        if (x.style.display === "none") {
            x.style.display = "block";
        }
    }