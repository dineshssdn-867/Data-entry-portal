
	async function getWebCam(){
    try{
        const videoSrc=await navigator.mediaDevices.getUserMedia({video:true});
        var video=document.getElementById("video");
        video.srcObject=videoSrc;
    }catch(e){
        console.log(e);
    }
}
getWebCam();
var capture=document.getElementById("capture");
var canvas=document.getElementById("canvas");
var context=canvas.getContext('2d');
var x=document.getElementById('myfile')
console.log(x)
//document.getElementById('download-photo').href = canvas.toDataURL('image/png');
capture.addEventListener("click",function(){
    context.drawImage(video,0,0,650,490);
});
console.log(canvas.toDataURL('image/png'))
	function myFunction() {
				return window.close();
		}