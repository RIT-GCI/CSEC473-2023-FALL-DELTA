const accurateTimer = (fn, time = 1000) => {
  let nextAt, timeout;
  nextAt = new Date().getTime() + time;

  const wrapper = () => {
    nextAt += time;
    timeout = setTimeout(wrapper, nextAt - new Date().getTime());
    fn();
  };

  const cancel = () => clearTimeout(timeout);

  timeout = setTimeout(wrapper, nextAt - new Date().getTime());

  return { cancel };
};

export default {
    data() {
      return {
        countDown: 300,
        visualCountdown: "5:00",
        timer: 10,
        services: {},
        blueTwoScore: 0,
        blueScore: 0,
        redScore: 0,
        rows: [],
      }
    },
    created() {
        // setTimeout(() => {
        //     this.getData();
        // }, 10000);
    },
    watch: {
        countDown: {
            handler(value) {
                if (value >= 0) {
                    if (this.countDown === 0) {
                        // Reset the countdown to 5 minutes after it reaches 0
                        this.getData();
                        this.countDown = 300;
                    } else {
                        setTimeout(() => {
                            this.countDown--;
                        }, 1000);
                    }
                }

                // Calculate minutes and seconds
                const minutes = Math.floor(this.countDown / 60);
                const seconds = this.countDown % 60;
                console.log(seconds)

                // Format visualCountdown as mm:ss
                this.visualCountdown = `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
            },
            immediate: true
        }
    },
    methods: {
        async getData() {
            console.log("Fetching");
            let response = await fetch("http://127.0.0.1:5000/display_scores");
    	    let body = await response.json();
    	    this.services = body.services;
    	    this.blueScore = body.scores.blue_score;
      	    this.blueTwoScore = body.scores.blue_two_score;
            this.redScore = body.scores.red_score;
    	    this.rows = [];

    	    for(let ip in this.services) {
        		let host = this.services[ip]
        		for(let service in host) {
        		    let status = host[service]
        		    console.log(host);
        	        this.rows.push({'ip': ip, 'service': service, 'status': status})
        		}
    	    }
    	},
        cancelUpdates() {
            this.timer.cancel();
        },
    },
    beforeUnmount() {
        this.cancelUpdates();
    },
    template: `
    <div class="timer_wrap">
        <h1 class="timer">{{visualCountdown}}</h1>
        <div class='scoreBox'>
            <div class="scoreDisplay">
                <h1>Red Team: {{redScore}}</h1>
                <h1>1st Blue Team: {{blueScore}}</h1>
                <h1>2nd Blue Team: {{blueTwoScore}}</h1>
            </div>
            
            <div class='scoreTable'>
                <table>
            	    <tr>
                        <th> Team </th>
            	        <th> IP </th>
            	        <th> Service </th>
            	        <th> Status </th>
            	    </tr>
            	    <tr v-for="row in rows">
                        <td> {{row.status[1]}} </td>
            	        <td> {{row.ip}} </td>
            	        <td> {{row.service}} </td>
            	        <td v-if='row.status[0]=="UP"'> <span class='dotUp'></span>  </td>
            	        <td v-else> <span class='dotDown'></span>  </td>
            	     </tr>
                </table>
            </div>
        </div>
    </div>
    `
  }