document.getElementById("form1").onsubmit=function() {

    result = calculateResult();

    document.getElementById("quizGrade").innerHTML = result;

    return false;
} 

function calculateResult(){
  if (document.getElementById("q1ans1").checked == false && 
  document.getElementById("q1ans2").checked == false && 
  document.getElementById("q1ans3").checked == false && 
  document.getElementById("q1ans4").checked == false) q1 = 0;
  else q1 = parseInt(document.querySelector('input[name = "q1"]:checked').value);
  if (document.getElementById("q2ans1").checked == false && 
  document.getElementById("q2ans2").checked == false && 
  document.getElementById("q2ans3").checked == false && 
  document.getElementById("q2ans4").checked == false) q2 = 0;
  else q2 = parseInt(document.querySelector('input[name = "q2"]:checked').value);
  if (document.getElementById("q3ans1").checked == false && 
  document.getElementById("q3ans2").checked == false && 
  document.getElementById("q3ans3").checked == false && 
  document.getElementById("q3ans4").checked == false) q3 = 0;
  else q3 = parseInt(document.querySelector('input[name = "q3"]:checked').value);
  if (document.getElementById("q4ans1").checked == false && 
  document.getElementById("q4ans2").checked == false && 
  document.getElementById("q4ans3").checked == false && 
  document.getElementById("q4ans4").checked == false) q4 = 0;
  else q4 = parseInt(document.querySelector('input[name = "q4"]:checked').value);
  if (document.getElementById("q5ans1").checked == false && 
  document.getElementById("q5ans2").checked == false && 
  document.getElementById("q5ans3").checked == false && 
  document.getElementById("q5ans4").checked == false) q5 = 0;
  else q5 = parseInt(document.querySelector('input[name = "q5"]:checked').value);
  if (document.getElementById("q6ans1").checked == false && 
  document.getElementById("q6ans2").checked == false && 
  document.getElementById("q6ans3").checked == false && 
  document.getElementById("q6ans4").checked == false) q6 = 0;
  else q6 = parseInt(document.querySelector('input[name = "q6"]:checked').value);
  if (document.getElementById("q7ans1").checked == false && 
  document.getElementById("q7ans2").checked == false && 
  document.getElementById("q7ans3").checked == false && 
  document.getElementById("q7ans4").checked == false) q7 = 0;
  else q7 = parseInt(document.querySelector('input[name = "q7"]:checked').value);
  if (document.getElementById("q8ans1").checked == false && 
  document.getElementById("q8ans2").checked == false && 
  document.getElementById("q8ans3").checked == false && 
  document.getElementById("q8ans4").checked == false) q8 = 0;
  else q8 = parseInt(document.querySelector('input[name = "q8"]:checked').value);
  if (document.getElementById("q9ans1").checked == false && 
  document.getElementById("q9ans2").checked == false && 
  document.getElementById("q9ans3").checked == false && 
  document.getElementById("q9ans4").checked == false) q9 = 0;
  else q9 = parseInt(document.querySelector('input[name = "q9"]:checked').value);
  if (document.getElementById("q10ans1").checked == false && 
  document.getElementById("q10ans3").checked == false) q10 = 0;
  else q10 = parseInt(document.querySelector('input[name = "q10"]:checked').value);

  return q1 + q2 + q3 + q4 + q5 + q6 + q7 + q8 + q9 + q10;
}


function reset (){
      $('.radiocheck').each(function(){
          $(this).prop('checked', unchecked);
  });
return false;
}

function submit(){
    const URL = '/get-coordinates'
	const xhr = new XMLHttpRequest();
	numberpass = calculateResult();
	sender = JSON.stringify(numberpass);
	xhr.open('POST', URL);
	xhr.send(sender);
}


