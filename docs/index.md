<!DOCTYPE html>

<html>

    <head>

        

        <style>
            #movingground {
                animation: slideright 55s infinite linear;
            }

            @keyframes slideright {
                from {
                    background-position: 10000px;
                    }

                to {
                    background-position: 0px;
                    }
            }
        </style>

    </head>

    <body>
        <script>
            counter = 0
            direction = "forward";
            flydirection = "down";
            amount = 160
            var scoreleft = 40
            var birdtop
            var birdstation
            var velocity = 1
            var signal
            var scorevalue = 0
            var PipeListLength
            var upsidedownpipe = false
            var rightsideuppipe = false
            var scorearray = []
            var pipeslist = []
            var pipeInt
            var moverightcount = -50
            var signal2
            const pipepos = 3

            var pressenter = document.createElement("div")
            pressenter.innerHTML = "Press Enter to Restart the Game."
            pressenter.style.position = "absolute"
            pressenter.style.right = "75px"
            pressenter.style.bottom = "75px"

            function ProcessScore(){
                birdscore.play()
                scorevalue += 1
                if (scorevalue == 10){
                    let scorevaluestring = JSON.stringify(scorevalue)
                    for(snumber in scorevaluestring){
                        let x = parseInt(scorevaluestring[snumber])
                        scorearray.push(x)
                    }
                    score.src = "/static/" + scorearray[0] + ".png"
                    background.appendChild(score2)     
                    score2.src = "/static/" + scorearray[1] + ".png"  

                } else if (scorevalue > 10 && scorevalue < 100){
                    scorearray = []
                    let scorevaluestring = JSON.stringify(scorevalue)
                    for(snumber in scorevaluestring){
                        let x = parseInt(scorevaluestring[snumber])
                        scorearray.push(x)
                    }
                    score.src = "/static/" + scorearray[0] + ".png"
                    score2.src = "/static/" + scorearray[1] + ".png"      

                } else if (scorevalue == 100){
                    scorearray = []
                    let scorevaluestring = JSON.stringify(scorevalue)
                    for(snumber in scorevaluestring){
                        console.log(scorevaluestring[snumber])
                        let x = parseInt(scorevaluestring[snumber])
                        scorearray.push(x)
                    }
                    score.src = "/static/" + scorearray[0] + ".png"
                    score2.src = "/static/" + scorearray[1] + ".png"
                    background.appendChild(score3)
                    score3.src = "/static/" + scorearray[2] + ".png"
                } else if (scorevalue > 100){
                    scorearray = []
                    let scorevaluestring = JSON.stringify(scorevalue)
                    for(snumber in scorevaluestring){
                        let x = parseInt(scorevaluestring[snumber])
                        scorearray.push(x)
                    }
                    score.src = "/static/" + scorearray[0] + ".png"
                    score2.src = "/static/" + scorearray[1] + ".png"
                    score3.src = "/static/" + scorearray[2] + ".png"
                } else {
                    score.src = "/static/" + scorevalue + ".png"
                }
            }

            function movepipes(individualpipe){
                individualpipe[2] += pipepos
                individualpipe[0].style.right = individualpipe[2] + "px"
                individualpipe[1].style.right = individualpipe[2] + "px"
                let pipeposition = individualpipe[0].getBoundingClientRect()
                let pipe2position = individualpipe[1].getBoundingClientRect()
                let birdposition = playerbird.getBoundingClientRect()
                let birdright = birdposition.right
                let birdleft = birdposition.left
                let birdtop = birdposition.top
                let birdbeneath = birdposition.bottom
                let pipe2left = pipe2position.left
                let pipe2right = pipe2position.right
                let pipe2top = pipe2position.top
                let pipeleft = pipeposition.left
                let piperight = pipeposition.right
                let pipebeneath = pipeposition.bottom

                if (birdright > pipeleft+8 && 
                    birdright < piperight && 
                    birdtop < (pipebeneath-450)){/*Bird's Face Hits Side of Pipe*/
                    signal2 = "finished"
                } else if (birdright > pipe2left+8 && 
                    birdbeneath-455 > pipe2top && 
                    birdright < pipe2right) {
                    signal2 = "finished"
                } else if(birdbeneath-455 > pipe2top &&
                    birdright > pipe2left+8 &&
                    birdright < pipe2right){
                    signal2 = "finished" 
                }  else if (individualpipe[2] > 500){
                    /*pipeslist.shift()*/
                    individualpipe[0].remove
                    individualpipe[1].remove
                } else if (birdleft > pipeleft-20 && birdright < piperight-17){
                    ProcessScore()
                }
            }

            function PipeOps(pipesarray){
                PipeListLength = pipesarray.length
                if (PipeListLength !== 0){
                    pipesarray.forEach(movepipes)    
                }
            }

            function Gravity(){
                let bgdetails = background.getBoundingClientRect()
                let bgbottom = bgdetails.bottom
                let bgtop = bgdetails.top
                let birddeets = playerbird.getBoundingClientRect()
                let birdtop = birddeets.top
                let birdbottom = birddeets.bottom;
                let birdheight = birddeets.height;

                amount += velocity
                velocity += 0.4

                if (birdtop < bgtop){
                    amount = bgtop
                    playerbird.style.top = amount + "px"
                    velocity = 0.7
                } else {
                playerbird.style.top = amount + "px"
                }

                if (birdbottom >= bgbottom){
                    var stoppos = (bgbottom) - birdheight
                    playerbird.style.top = (stoppos) + "px"
                    velocity = 0
                    return "finished"
                }
            }

            function Jump(){
                velocity = -7.6 
                birdjump.play()
            }

            function MainGameLoop(){
                signal = Gravity()
                if (signal === "finished" || signal2 === "finished"){
                    birdhit.play()
                    birdfail.play()
                    clearInterval(myTime)
                    ground.style.animationPlayState = 'paused';
                    clearInterval(pipeInt)
                    ground.appendChild(pressenter)
                    document.body.onkeyup = function(event){
                        if(event.keyCode == 32){

                        } else if (event.keyCode == 13){
                            location.reload()
                        }
                    }
                    window.cancelAnimationFrame(stopgame)
                } else {
                    PipeOps(pipeslist)
                    var stopgame = requestAnimationFrame(MainGameLoop)
                }
            }

            background = document.createElement("div")
            background.style.height = "490px" /*Correct height is 580px*/
            background.style.width = "420px" 
            background.style.margin = "auto"
            background.style.backgroundSize = "100%"
            background.style.backgroundImage = "url('/static/fbbackground.png')"
            background.style.overflow = "hidden"
            background.style.position = "relative"
            document.body.appendChild(background)

            ground = document.createElement("div")
            ground.id = "movingground"
            ground.style.backgroundImage = "url('/static/fbground.png')"
            ground.style.backgroundSize = "100%"
            ground.style.backgroundRepeat = "repeat-x"
            ground.style.animationPlayState = 'running';
            ground.style.height = "137px" /*Correct height is 115px*/
            ground.style.width = "420px"
            ground.style.right = "590px"
            ground.style.position = "absolute"
            ground.style.top = "490px"
            document.body.appendChild(ground)

            picarray = ["/static/Upbird.png",
                        "/static/Midbird1.png",
                        "/static/Midbird2.png",
                        "/static/Downbird.png"]
            playerbird = new Image()
            playerbird.src = "/static/Upbird.png"
            playerbird.style.position = "absolute"
            playerbird.style.left = "145px"
            playerbird.style.height = "45px"
            playerbird.style.width = "60px"
            playerbird.style.top = "200px"
            birdjump = new Audio("/static/jump.mp3");
            birdhit = new Audio("/static/audio_hit.wav")
            birdfail = new Audio("static/audio_die.ogg")
            birdscore = new Audio("/static/audiopoint.wav")
            background.appendChild(playerbird)

            title = new Image()
            title.src = "/static/FlappyBirdTitleText.jpg"
            title.style.position = "absolute"
            title.style.left = "135px"
            title.style.top = "20px"
            title.style.width = "150px"
            title.style.margin = "auto"
            background.appendChild(title)

            score = new Image()
            score.src = "/static/" + scorevalue + ".png"
            score.style.position = "absolute"
            score.style.height = "27px"
            score.style.width = "20px"

            score2 = new Image()
            score2.src = "/static/" + scorevalue + ".png"
            score2.style.position = "absolute"
            score2.style.height = "27px"
            score2.style.top = "30px"
            score2.style.left = scoreleft + "px"
            score2.style.width = "20px"

            score3 = new Image()
            score3.src = "/static/" + scorevalue + ".png"
            score3.style.position = "absolute"
            score3.style.height = "27px"
            score3.style.top = "30px"
            score3.style.left = (scoreleft+(scoreleft/2)) + "px"
            score3.style.width = "20px"

            var myTime = setInterval(function(){/*SetInterval to show image from array*/
                function Animate(picindex){
                    playerbird.src = picarray[picindex]
                }

                if (counter === 0 || direction === "forward"){
                    direction = "forward"
                    Animate(counter)
                    counter += 1
                    if (counter === 3){
                        direction = "backward"
                    } 
                } else if (counter === 3 || direction === "backward"){
                        Animate(counter)
                        counter -= 1
                    }
                },100)

            function movebird(){ /*Bird floating in Title Screen*/
                if (flydirection === "down"){
                    amount += 2
                    playerbird.style.top = amount + "px";
                    titlefloat = window.requestAnimationFrame(movebird)
                    if (amount === 240){
                        flydirection = "up"
                    }
                } else {
                    amount -= 2
                    playerbird.style.top = amount + "px";
                    titlefloat = window.requestAnimationFrame(movebird)
                    if (amount === 160){
                        flydirection = "down"
                    }
                }
            }

            titlefloat = window.requestAnimationFrame(movebird)

            function startgame(){
                cancelAnimationFrame(titlefloat)
                score.style.top = "30px";
                score.style.left = "20px";
                background.appendChild(score)
                title.remove()
                document.removeEventListener("keydown", startgame)
                document.body.onkeyup = function(event){
                    if(event.keyCode == 32){
                        window.requestAnimationFrame(Jump)
                    }
                }
                playerbird.style.top = amount + "px"

                pipeInt = setInterval(function(){
                    let bottompheight = Math.floor(Math.random() * (451-189) + 189)
                    let toppheight = bottompheight - 450
                    var pipetop = 0
                    var pipebottom = 0

                    pipetop = new Image()
                    pipetop.src = "/static/flappybird-pipe.png"
                    pipetop.style.position = "absolute"
                    pipetop.style.top = toppheight + "px" /*bottom pipe has to be +450 of this number, the greater the number, the lower the pipe, highest is 1*/
                    pipetop.style.right = moverightcount + "px"
                    pipetop.style.transform = "rotate(180deg)"
                    background.appendChild(pipetop)

                    pipebottom = new Image()
                    pipebottom.src = "/static/flappybird-pipe.png"
                    pipebottom.style.position = "absolute"
                    pipebottom.style.top = bottompheight + "px" /*lowest number this can be is 189px, highest is 450, -450 for above number*/
                    pipebottom.style.right = moverightcount + "px"
                    background.appendChild(pipebottom)

                    pipeslist.push([pipebottom, pipetop, moverightcount])

                }, 1500);

                window.requestAnimationFrame(MainGameLoop)
            }

            document.addEventListener("keydown", startgame)
        </script>
    </body>

</html>
