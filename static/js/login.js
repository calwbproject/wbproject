const login_form = document.getElementById("login_form");
const login_button = document.getElementById("login_button");
const logout_button = document.getElementById("logout_button");
const message = document.getElementById("successH1");

//버튼을 누르면 폼 제출이 실행됨
login_button.addEventListener("click", async (e) => {
  const url = login_form.action;
  const username = login_form.querySelector('[name="username"]').value;
  const password = login_form.querySelector('[name="password"]').value;

  //보내는 정보
  const payload = { username, password };

  try {
    //포스트 방식,컨텐츠 타입은 application/json, 바디는 payload를 json화 시켜서 전송
    const response = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    const data = await response.json();

    console.log(data);
    //응답이 정상이면 실행
    if (response.ok) {
      login_form.style.display = "none";
      document.getElementById("successH1").style.display = "block";

      //로컬세션에 저장
      localStorage.setItem("access", data.access);
      localStorage.setItem("refresh", data.refresh);

      //메시지와 로그아웃 버튼 출력
      message.style.display = "block";
      logout_button.style.display = "";
    }
    //오류가 발생하면 오류를 출력
  } catch (e) {
    console.error(err);
    alert("error in login");
  }
});

logout_button.addEventListener("click", () => {
  //세션 삭제
  localStorage.removeItem("access");
  localStorage.removeItem("refresh");
  logout_button.style.display = "none";

  //로그인 상태로 복귀
  login_form.style.display = "";
  message.style.display = "none";
});
