// function togglePopup(){
//     document.getElementById("popup-1").classList.toggle("active");
// }
// function togglePopup(){
//     document.getElementById("popup-2").classList.toggle("active");
// }
// function togglePopup(){
//     document.getElementById("popup-3").classList.toggle("active");
// }
// function togglePopup(){
//     document.getElementById("popup-4").classList.toggle("active");
// }
// function togglePopup(){
//     document.getElementById("popup-5").classList.toggle("active");
// }


let ids=["popup-1","popup-2","popup-3","popup-4","popup-5"];
function togglePopup(ids){
        for(let i=0;i<=ids.length;i++){
            const id=ids[i];
            document.getElementById(id).classList.toggle("active");
        }
}