
function getTime() {
    var Now = new Date();
    var NowTime = Now.getFullYear();
    
    NowTime += '-' + String(Number(Now.getMonth()) +1) ;
    NowTime += '-' + Now.getDate();
    NowTime += ' ' + Now.getHours();
    NowTime += ':' + Now.getMinutes();
    NowTime += ':' + Now.getSeconds();
    return NowTime;
}

//경기신청모달 고가 평균 폼 확인
function goga_form_check(data){
    data_=data.split(':')

    if(data.length != 8)
        return false;
    else if(data[2] != ':')
        return false;
    else if(data[5] != ':')
        return false;
    else if(isNaN(data_[0]))
        return false;
    else if(isNaN(data_[1]))
        return false;
    else if(isNaN(data_[2]))
        return false;

    return true;
}
//경기신청모달 경기 날짜 폼 체크
function match_date_form_check(match_date) {
    if(match_date.length != 10) 
        return false;
    else if(match_date[4] != '-')
        return false;
    else if(match_date[7] != '-')
        return false;
    
    match_date_=match_date.split('-')

    if(isNaN(match_date_[0]))
        return false;
    else if(isNaN(match_date_[1]))
        return false;
    else if(isNaN(match_date_[2]))
        return false;

    return true;
}
//경기신청 모달 시간 체크
function time_form_check(time){
    if(time.length != 5)
        return false;
    else if(time[2] != ':')
        return false;

    time_=time.split(':')
    if(isNaN(time_[0]))
        return false;
    else if (isNaN(time_[1]))
        return false;
    return true;
}

//경기 신청모달에서 참여인원 수 선택시
$('#modal_fmatch_select').change(function(e) {
    console.log("change1")
    var state=$('#modal_fmatch_select option:selected').val();
    if( state== '2'){
        $('#modal_fmatch_blue_p3_name').attr('disabled',true);
        $('#modal_fmatch_blue_p4_name').attr('disabled',true);
    }
    else if( state== '3'){
        console.log("change")
        $('#modal_fmatch_blue_p3_name').attr('disabled',false);
        $('#modal_fmatch_blue_p4_name').attr('disabled',true);
    }
    else if( state== '4'){
        $('#modal_fmatch_blue_p3_name').attr('disabled',false);
        $('#modal_fmatch_blue_p4_name').attr('disabled',false);
    }
})

//모달에서 로그인 버튼 클릭
$(document).on('click', '#modal_signin_btn', function(e) {
    var player_name = $('#modal_player_name').val();
    var player_passwd = $('#modal_player_passwd').val(); 

    console.log(player_name);
    console.log(player_passwd);
    $.ajax({
        url:"{% url 'hzm:ajax_signin' %}",
        type:'POST',
        data : {
            'player_name' : player_name,
            'player_passwd' : player_passwd,
            'csrfmiddlewaretoken' : "{{csrf_token}}",

        },
        success:function(msg) {
            console.log("login: "+msg);
            if( msg=="login_fail1") {
                return swal("존재하지 않는 아이디입니다");
            }
            else if (msg=="login_fail2") {
                return swal("잘못된 접근입니다.");
            }
            else if(msg=="login_fail3"){
                return swal("존재하지 않는 아이디입니다");
            }
            else if(msg=="auth_fail"){
                return swal("승인 대기중입니다 잠시만 기다려주세요!");
            }
            else {
                location.reload();
            }
        },
        error : function(error) {
            swal("아이디/비밀번호가 일치하지 않습니다.");
        }
    });
});

//로그아웃 버튼 클릭
$(document).on('click','#logout_btn', function(e) {
    $.ajax({
        url:"{% url 'hzm:ajax_logout' %}",
        type:'GET',
        success:function(data) {
            swal("바이바이~");
            location.reload();
        },
        error : function(error) {
            swal("실패");
        }
    })
});



/*
var blank_pattern = /[\s]/g;

function getTime() {
    var Now = new Date();
    var NowTime = Now.getFullYear();
    
    NowTime += '-' + String(Number(Now.getMonth()) +1) ;
    NowTime += '-' + Now.getDate();
    NowTime += ' ' + Now.getHours();
    NowTime += ':' + Now.getMinutes();
    NowTime += ':' + Now.getSeconds();
    return NowTime;
}

        //경기신청모달 고가 평균 폼 확인
function goga_form_check(data){
    data_=data.split(':')

    if(data.length != 8)
        return false;
    else if(data[2] != ':')
        return false;
    else if(data[5] != ':')
        return false;
    else if(isNaN(data_[0]))
        return false;
    else if(isNaN(data_[1]))
        return false;
    else if(isNaN(data_[2]))
        return false;

    return true;
}
//경기신청모달 경기 날짜 폼 체크
function match_date_form_check(match_date) {
    if(match_date.length != 10) 
        return false;
    else if(match_date[4] != '-')
        return false;
    else if(match_date[7] != '-')
        return false;
    
    match_date_=match_date.split('-')

    if(isNaN(match_date_[0]))
        return false;
    else if(isNaN(match_date_[1]))
        return false;
    else if(isNaN(match_date_[2]))
        return false;

    return true;
}
//경기신청 모달 시간 체크
function time_form_check(time){
    if(time.length != 5)
        return false;
    else if(time[2] != ':')
        return false;

    time_=time.split(':')
    if(isNaN(time_[0]))
        return false;
    else if (isNaN(time_[1]))
        return false;
    return true;
}
//경기신청 버튼
$(document).on('click','#modal_fmatch_btn',function(e) {
    var blue_goga_avg = $('#modal_fmatch_blue_goga_avg').val();
    var formData = new FormData();
    var post_writer = $('#modal_fmatch_name').val();
    var club_name = $('#modal_fmatch_clubname').val();
    var match_date = $('#modal_fmatch_date').val();
    var match_time_start = $('#modal_fmatch_time_start').val();
    var match_time_end = $('#modal_fmatch_time_end').val();
    var player_num = $('#modal_fmatch_select').val();
    var passwd = $('#modal_fmatch_passwd').val();
    var player = Array();
    var date = getTime();
    var player_count=0;
    
    for(var i = 0; i <player_num; i++) {
            player[i] = $('#modal_fmatch_blue_p'+(i+1)+'_name').val();
            if($.trim(player[i]) != '') {
                player_count++;
                console.log("player["+i+"]:"+player[i]);
            }
    }


    if( $.trim(club_name) == '') {
        console.log("club_name :" +club_name)
        return swal("클럽명을 입력해주세요");
    }
    else if($.trim(post_writer) == '') {
         console.log("post writer: "+ club_name)
        return swal("카러플 닉네임을 입력해주세요");
    }
    else if(player_num != player_count){
        console.log("player_num :"+player_num)
        console.log("player_num input :"+player.length)
        return swal("라이더를  입력해 주세요");
    }
    else if(!(match_date)){
        console.log("match date : "+match_date)
        return swal("희망 경기 날짜를 입력해주세요 ex)2020-01-01");
    }
    else if(match_date_form_check(match_date) == false){
        return swal("희망 경기 날짜를 입력해주세요 ex)2020-01-01");
    }
    else if(goga_form_check(blue_goga_avg) == false) {	
        return swal("고가 입력 양식 00:00:00");
    } 
    else if(time_form_check(match_time_start) == false || time_form_check(match_time_end) == false){
        return swal("시간 입력 양식 ex) 11:11")
    }
    else if(!(match_time_start))
        return swal("시작 시간을 입력해주세요");
    else if(!(match_time_end))
        return swal("종료 시간을 입력해주세요");
    else if(match_time_start > match_time_end)
        return swal("시작시간이 종료시간보다 늦습니다!");
    else if(!(passwd))
        return swal("비밀번호를 입력해주세요");

    console.log("match date : "+match_date);
    console.log(match_time_start);
    console.log(match_time_end);

    swal({
        title: "이길 수 있겠어?",
        text: "무르기 없기~",
        icon: "warning",
        buttons: true,
        dangerMode: true,
    })
    .then((willDelete) => {
        if (willDelete) {

            formData.append('csrfmiddlewaretoken','{{ csrf_token }}');
            formData.append('p1',player[0]);
            formData.append('p2',player[1]);
            formData.append('p3',player[2]);
            formData.append('p4',player[3]);
            formData.append('post_writer',post_writer);
            formData.append('club_name',club_name);
            formData.append('match_date',match_date);
            formData.append('match_time_start',match_time_start);
            formData.append('match_time_end',match_time_end);
            formData.append('player_num',player_num);
            formData.append('passwd',passwd);
            formData.append('blue_goga_avg',blue_goga_avg);
            formData.append('date',date);
            console.log("date : "+date)
            $.ajax({
                url : "{% url 'hzm:ajax_add_fmatch' %}",
                type : 'POST',
                contentType : false,
                processData : false,
                data : formData,
                success : function(data) {
                    $('#friendlymatch').modal('hide');
                    swal("신청완료", "수락 완료되면 경기결과에서 확인 하 실 수 있어요!", "success");
                    
                },
                error : function(error) {
                    swal("신청실패", "아마도 통신오류??..", "error");
                    $('#friendlymatch').modal('hide');
                },
            });



        } else {
            swal("담에 봐요!");
            $('#friendlymatch').modal('hide');
        }
    });

});

//로그아웃 버튼 클릭
$(document).on('click','#logout_btn', function(e) {
    $.ajax({
        url:"{% url 'hzm:ajax_logout' %}",
        type:'GET',
        success:function(data) {
            swal("바이바이~");
            location.reload();
        },
        error : function(error) {
            swal("실패");
        }
    })
});


//중복확인 버튼 클릭시
function id_check_btn(player_name){
    console.log(player_name);
    name = player_name;

    if(blank_pattern.test(name)==true || name=='')
        return swal("공백은 입력이 안됩니다~")

    $.ajax({
        url : "{% url 'hzm:ajax_id_check_btn' %}",
        type:'GET',
        data :{
            'player_name' : name,
        },
        success: function(msg) {
            if(msg=="error" || msg=="fail"){
                swal("이미 존재하는 닉네임 입니다.")
            }
            else
            {
                swal("사용 가능한 닉네임 입니다.");
            }
        },
        error : function(msg) {
            swal("아이디 중복체크 에러, 관리자 문의");
        }
    })
}
$(document).on('click','#modal_mypage_check_id_btn',function(e) {
    var name = $('#mypage_player_name').val();
    console.log("name : "+name);
    id_check_btn(name);
});

//마이룸 정보수정
$(document).on('click','#mypage_info_edit_btn',function(e){
    var player_name = $('#mypage_player_name').val();
    var password_now = $('#mypage_password_now').val();
    var password_change = $('#mypage_password_change').val();

    console.log("edit infdo mypage")
    console.log(password_now)
    console.log(password_change)
    if(!(password_now))
        return swal("비밀번호를 입력해주세요.")
    else if(password_now == password_change){
        $('#mypage_password_now').val('');
        $('#mypage_password_change').val('');
        return swal("이전 비밀번호와 달라야 합니다");
    }
    else {
        $.ajax({
            url : "{% url 'hzm:ajax_edit_mypage_info' %}",
            type:'POST',
            dataType:'json',
            data: {
                'csrfmiddlewaretoken':'{{csrf_token}}',
                'player_name':player_name,
                'password_now' : password_now,
                'password_change':password_change,
            },
            success:function(data) {
                if(data.msg=="good"){
                    $('#mypage-title').text(data.player_name+'의 마이룸')
                    swal("변경성공")
                }
                else if(data.msg=="sameId"){
                    swal("중복된 닉네임입니다.")
                }
                else if(data.msg=="fail" || data.msg=="passwordfail")
                    swal("비밀번호가 일치하지 않습니다.")
                    $('#mypage_password_change').val('')
                    $('#mypage_password_now').val('')
            }
        });
    }
});
//경기 신청모달에서 참여인원 수 선택시
$('#modal_fmatch_select').change(function(e) {
    console.log("change1")
    var state=$('#modal_fmatch_select option:selected').val();
    if( state== '2'){
        $('#modal_fmatch_blue_p3_name').attr('disabled',true);
        $('#modal_fmatch_blue_p4_name').attr('disabled',true);
    }
    else if( state== '3'){
        console.log("change")
        $('#modal_fmatch_blue_p3_name').attr('disabled',false);
        $('#modal_fmatch_blue_p4_name').attr('disabled',true);
    }
    else if( state== '4'){
        $('#modal_fmatch_blue_p3_name').attr('disabled',false);
        $('#modal_fmatch_blue_p4_name').attr('disabled',false);
    }
})

*/