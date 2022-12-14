import Deta from 'deta'; // import Deta

// Initialize with a Project Key
const deta = Deta('project key');

// This how to connect to or create a database.
const db = deta.Base('simple_db');

new Vue({

  el: "#app",
  data() {
    return {
      audio: null,
      circleLeft: null,
      barWidth: null,
      duration: null,
      currentTime: null,
      isTimerPlaying: false,
      tracks: [

        {
          name: "Ew",
          artist: "Joji",
          cover: "https://raw.githubusercontent.com/akshzyx/playerzyx/master/img/nectar-joji.jpg",
          source: "https://ipfs.io/ipfs/bafybeifj664nr4q4o46tzc42nvdgzn3ceafxfddha7amocaawjvjfcervm",
          url: "https://www.youtube.com/watch?v=UGB_Bsm5Unk",
          favorited: false
        }
        // },
        // {
        //   name: "Tick Tock",
        //   artist: "Joji",
        //   cover: "https://raw.githubusercontent.com/akshzyx/playerzyx/master/img/nectar-joji.jpg",
        //   source: "https://raw.githubusercontent.com/akshzyx/playerzyx/master/mp3/Tick Tock.mp3",
        //   url: "https://www.youtube.com/watch?v=2FCo7OxVoeY",
        //   favorited: false
        // },
        // {
        //   name: "Daylight",
        //   artist: "Joji, Diplo",
        //   cover: "https://raw.githubusercontent.com/akshzyx/playerzyx/master/img/Daylight-joji.jpg",
        //   source: "https://raw.githubusercontent.com/akshzyx/playerzyx/master/mp3/Daylight.mp3",
        //   url: "https://www.youtube.com/watch?v=v97FPN2US2o",
        //   favorited: false
        // },
        // {
        //   name: "Gimme Love",
        //   artist: "Joji",
        //   cover: "https://raw.githubusercontent.com/akshzyx/playerzyx/master/img/nectar-joji.jpg",
        //   source: "https://raw.githubusercontent.com/akshzyx/playerzyx/master/mp3/Gimme Love.mp3",
        //   url: "https://www.youtube.com/watch?v=jPan651rVMs",
        //   favorited: false
        // },
        //
        // {
        //   name: "Sanctuary",
        //   artist: "Joji",
        //   cover: "https://raw.githubusercontent.com/akshzyx/playerzyx/master/img/nectar-joji.jpg",
        //   source: "https://raw.githubusercontent.com/akshzyx/playerzyx/master/mp3/Sanctuary.mp3",
        //   url: "https://www.youtube.com/watch?v=YWN81V7ojOE",
        //   favorited: true
        // },
        // {
        //   name: "NITROUS",
        //   artist: "Joji",
        //   cover: "https://raw.githubusercontent.com/akshzyx/playerzyx/master/img/nectar-joji.jpg",
        //   source: "https://raw.githubusercontent.com/akshzyx/playerzyx/master/mp3/NITROUS.mp3",
        //   url: "https://www.youtube.com/watch?v=dHq_AS62ioY",
        //   favorited: true
        // },
        // {
        //   name: "Pretty Boy (feat. Lil Yachty)",
        //   artist: "Joji, Lil Yachty",
        //   cover: "https://raw.githubusercontent.com/akshzyx/playerzyx/master/img/nectar-joji.jpg",
        //   source: "https://raw.githubusercontent.com/akshzyx/playerzyx/master/mp3/Pretty Boy.mp3",
        //   url: "https://www.youtube.com/watch?v=Qn5IpWXWub0",
        //   favorited: true
        // },
        // {
        //   name: "Like You Do",
        //   artist: "Joji",
        //   cover: "https://raw.githubusercontent.com/akshzyx/playerzyx/master/img/nectar-joji.jpg",
        //   source: "https://raw.githubusercontent.com/akshzyx/playerzyx/master/mp3/Like You Do.mp3",
        //   url: "https://www.youtube.com/watch?v=Bv-1BnoB75k",
        //   favorited: true
        // }
      ],
      currentTrack: null,
      currentTrackIndex: 0,
      transitionName: null
    };
  },
  
  methods: {
    load(){

    },
    play() {
      if (this.audio.paused) {
        this.audio.play();
        this.isTimerPlaying = true;
      } else {
        this.audio.pause();
        this.isTimerPlaying = false;
      }
    },
    async onsubmit() {

      var ipfsHash;
      const url = document.getElementById("URL").value
      console.log(url)
      alert("Received Song Request" + url)
      if (url === "Enter your YouTube URL...") {
        alert("Enter Again")
      }
      await db.put({name: "alex", age: 77})
      let res = await db.fetch();
      let allItems = res.items;

      // continue fetching until last is not seen
      allItems.forEach( (item)=>{
        alert(item)
          }
      )
      // else {
      //   await fetch("https://thv6stbw3kp24elb42iaiemodu0xcvqe.lambda-url.us-east-2.on.aws/ " + url)
      //       .then((data) => {
      //         data.json().then( (data) => {
      //           console.log('Success:', data);
      //           ipfsHash = data["body"]
      //           console.log(ipfsHash)
      //           URL = url
      //           video_id = url.slice(-11)
      //           console.log(video_id)
      //           fetch("https://jvjrj4.deta.dev/metadata/"+video_id)
      //               .then((response) => {
      //                 console.log(response)
      //                   response.json().then( (response) => {
      //                   console.log(response)
      //                   const artist = response["author"]
      //                   const title = response["title"]
      //                   const cover = response["thumbnail"]
      //                   const url = response["url"]
      //                   console.log(artist)
      //                   console.log(title)
      //                   console.log(cover)
      //
      //           this.tracks.push(
      //               {
      //                 name: title,
      //                 artist: artist,
      //                 cover: cover,
      //                 source: "https://" + ipfsHash + ".ipfs.cf-ipfs.com",
      //                 url: url,
      //                 favorited: false
      //               }
      //           )
      //                 alert("FINISHED UPLOAD")
      //
      //         })
      //                  })
      //       })
      //         })
      //
      //
      // }
    }
    ,
    generateTime() {
      let width = (100 / this.audio.duration) * this.audio.currentTime;
      this.barWidth = width + "%";
      this.circleLeft = width + "%";
      let durmin = Math.floor(this.audio.duration / 60);
      let dursec = Math.floor(this.audio.duration - durmin * 60);
      let curmin = Math.floor(this.audio.currentTime / 60);
      let cursec = Math.floor(this.audio.currentTime - curmin * 60);
      if (durmin < 10) {
        durmin = "0" + durmin;
      }
      if (dursec < 10) {
        dursec = "0" + dursec;
      }
      if (curmin < 10) {
        curmin = "0" + curmin;
      }
      if (cursec < 10) {
        cursec = "0" + cursec;
      }
      this.duration = durmin + ":" + dursec;
      this.currentTime = curmin + ":" + cursec;
    },
    updateBar(x) {
      let progress = this.$refs.progress;
      let maxduration = this.audio.duration;
      let position = x - progress.offsetLeft;
      let percentage = (100 * position) / progress.offsetWidth;
      if (percentage > 100) {
        percentage = 100;
      }
      if (percentage < 0) {
        percentage = 0;
      }
      this.barWidth = percentage + "%";
      this.circleLeft = percentage + "%";
      this.audio.currentTime = (maxduration * percentage) / 100;
      this.audio.play();
    },
    clickProgress(e) {
      this.isTimerPlaying = true;
      this.audio.pause();
      this.updateBar(e.pageX);
    },
    prevTrack() {
      this.transitionName = "scale-in";
      this.isShowCover = false;
      if (this.currentTrackIndex > 0) {
        this.currentTrackIndex--;
      } else {
        this.currentTrackIndex = this.tracks.length - 1;
      }
      this.currentTrack = this.tracks[this.currentTrackIndex];
      this.resetPlayer();
    },
    nextTrack() {
      this.transitionName = "scale-out";
      this.isShowCover = false;
      if (this.currentTrackIndex < this.tracks.length - 1) {
        this.currentTrackIndex++;
      } else {
        this.currentTrackIndex = 0;
      }
      this.currentTrack = this.tracks[this.currentTrackIndex];
      this.resetPlayer();
    },
    resetPlayer() {
      this.barWidth = 0;
      this.circleLeft = 0;
      this.audio.currentTime = 0;
      this.audio.src = this.currentTrack.source;
      setTimeout(() => {
        if(this.isTimerPlaying) {
          this.audio.play();
        } else {
          this.audio.pause();
        }
      }, 300);
    },
    favorite() {
      this.tracks[this.currentTrackIndex].favorited = !this.tracks[
        this.currentTrackIndex
      ].favorited;
    }
  },
  created() {
    let vm = this;
    this.currentTrack = this.tracks[0];
    this.audio = new Audio();
    this.audio.src = this.currentTrack.source;
    this.audio.ontimeupdate = function() {
      vm.generateTime();
    };
    this.audio.onloadedmetadata = function() {
      vm.generateTime();
    };
    this.audio.onended = function() {
      vm.nextTrack();
      this.isTimerPlaying = true;
    };

    // this is optional (for preload covers)
    for (let index = 0; index < this.tracks.length; index++) {
      const element = this.tracks[index];
      let link = document.createElement('link');
      link.rel = "prefetch";
      link.href = element.cover;
      link.as = "image"
      document.head.appendChild(link)
    }
  }
});
