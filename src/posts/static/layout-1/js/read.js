var winheight, docheight, trackLength, throttlescroll


function getmeasurements(){
    winheight= window.innerHeight || (document.documentElement || document.body).clientHeight
    docheight = $(document).height()
    trackLength = docheight - winheight
    return docheight, winheight
}
 
function amountscrolled(){
    getmeasurements()
    var scrollTop = window.pageYOffset || (document.documentElement || document.body.parentNode || document.body).scrollTop
    var pctScrolled = Math.floor(scrollTop/trackLength * 100) // gets percentage scrolled (ie: 80 or NaN if tracklength == 0)
    // console.log('docheight'+docheight)
    // console.log('winheight'+winheight)
    // console.log('scrollTop'+scrollTop)
    console.log(pctScrolled + '% scrolled')
}
  
// window.addEventListener("resize", function(){
//     getmeasurements()
// }, false)
 
window.addEventListener("scroll", function(){
    clearTimeout(throttlescroll)
        throttlescroll = setTimeout(function(){ // throttle code inside scroll to once every 50 milliseconds
        amountscrolled()
    }, 50)
}, false)

