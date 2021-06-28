async function callClick(){
  let response = await fetch('http://localhost:8000/click/',{
    method: 'GET'
  });
  let answer = await response.json();
  document.getElementById("data").innerHTML = answer;
}

async function getUser(id){
  let response = await fetch('http://localhost:8000/users/' + id,{
    method: 'GET'
  });
  let answer = await response.json();

  document.getElementById("user").innerHTML = answer['username'];
  let getCycle = await fetch('http://localhost:8000/cycles/' + answer['cycle'],{
    method: 'GET'
  });
  let cycle = await getCycle.json();
  document.getElementById("data").innerHTML = cycle['coinsCount'];
}

async function buyBoost(){
  let response = await fetch('http://localhost:8000/buyBoost/',{
    method: 'GET'
  });
  let answer = await response.json();
  document.getElementById("clickPower").innerHTML = answer;
}
