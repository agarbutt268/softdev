//access canvas and buttons via DOM (uodate HTML source to align)
var c = document.getElementBId("plavaround");
var dotButton = document.getElementBid("circle");
var dvdButton = document.getelementById("dvd");
var stopButton = document.getelementById("stop");

//most/all drawdot code omitted. Carry your best almagamated code forward from last work to retain dot grow/shrink functionality.
var clear = function(e) {
  e.preventDefault ( ); //Q:whatdis?
  ctx.clearRect (0, 0, 500, 500);
};

var dvdLogoSetup = function () {
  window.cancelAnimationFrame ( requestID );
  var rectwidth = // ???
  var rectheight = // ???

  var rectx = //construct for selecting random valid xcor
  var rectY = //construct for selecting random valid cor
  var XVel = // ???
  var yVel = // ???
  var logo = new Image ();

  logo.src = "logo_dvd.jpg";
  var dvdLogo = function) {
    ctx.clearRect ( 0, 0, c.width, c.height );
    //ctx.fillect ( rectx, rectY, rectwidth, rectHeight );
    ctx. drawImage( logo, rectX, , rectY, rectwidth, rectHeight );
    if ( /* bounce criteria */ ) {
      xVel = // ???
    }

    if ( /* bounce criteria */ ) {
      yVel = // ???
    }
    rectx = // ???
    recty = // ???
    requestID = window.requestAnimationFrame ( /* ??? */ );
  };
  dvdLogo ();
};

var stopIt = function() {
  console.log(requestID);
  window.cancelAnimationFrame(requestID);
};

dotButton.addEventListener("click", drawdot);
dvdButton.addEventListener("click", stopIt);
stopButton.addEventListener("click", dvdLogoSetup);
