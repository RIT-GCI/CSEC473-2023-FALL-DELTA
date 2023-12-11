import { ref, createApp } from 'vue';

export default {
  data() {
    return {
      services: {},
      redScore: 0,
      blueTwoScore: 0,
      blueScore: 0,
      rows: [],
    };
  },
  methods: {
    async getData() {
      console.log("Fetching");
      try {
        let response = await fetch("http://127.0.0.1:5000/display_scores");
        let body = await response.json();
        this.services = body.services;
        this.blueScore = body.scores.blue_score;
        this.blueTwoScore = body.scores.blue_two_score;
        this.redScore = body.scores.red_score;
        this.rows = [];
        for (let ip in this.services) {
          let host = this.services[ip];
          for (let service in host) {
            let status = host[service];
            this.rows.push({ ip: ip, service: service, status: status });
          }
        }
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    },
    async incrementBlueScore(sub) {
      const blue_value = this.$refs.blue_input.value || 0;
      try {
        let formData = new FormData();

        if (sub) {
          this.blueScore = (parseInt(this.blueScore) - parseInt(blue_value)).toString();
        } else {
          this.blueScore = (parseInt(this.blueScore) + parseInt(blue_value)).toString();
        }
        
        formData.append('blue_score', this.blueScore);
        let response = await fetch("http://127.0.0.1:5000/increment_blue_score", {
          method: "POST",
          body: formData,
        });
      } catch (error) {
        console.error("Error incrementing blue score:", error);
      }
    },
    async incrementBlueTwoScore(sub) {
      const blue_two_input = this.$refs.blue_two_input.value || 0;
      try {
        let formData = new FormData();

        if (sub) {
          this.blueTwoScore = (parseInt(this.blueTwoScore) - parseInt(blue_two_input)).toString();
        } else {
          this.blueTwoScore = (parseInt(this.blueTwoScore) + parseInt(blue_two_input)).toString();
        }
        
        formData.append('blue_two_score', this.blueTwoScore);
        let response = await fetch("http://127.0.0.1:5000/increment_blue_two_score", {
          method: "POST",
          body: formData,
        });
      } catch (error) {
        console.error("Error incrementing blue two score:", error);
      }
    },
    async incrementRedScore(sub) {
      const red_value = this.$refs.red_input.value || 0;
      try {
        let formData = new FormData();

        if (sub) {
          this.redScore = (parseInt(this.redScore) - parseInt(red_value)).toString();
        } else {
          this.redScore = (parseInt(this.redScore) + parseInt(red_value)).toString();
        }
        
        formData.append('red_score', this.redScore);
        let response = await fetch("http://127.0.0.1:5000/increment_red_score", {
          method: "POST",
          body: formData,
        });
      } catch (error) {
        console.error("Error incrementing red score:", error);
      }
    },
  },
  created() {
    this.getData();
    this.timer = setInterval(this.getData, 60000);
  },
  template: `
    <div class="scoring">
      <div class="score_box">
          <h1 style="color: white;">Red Score: <span style="color: red;">{{redScore}}</span></h1>
          <input type="number" name="blue_manual_scoring" ref="red_input" min="0">
          <div class="choices" style="width: 25%;">
            <button @click="incrementRedScore(false)">Add</button>
            <button @click="incrementRedScore(true)">Sub</button>
          </div>
      </div>
      <br>
      <div class="score_wrap">
        <div class="score_box">
          <h1>Blue One Score</h1>
          <input type="number" name="blue_manual_scoring" ref="blue_input" min="0">
          <div class="choices">
            <button @click="incrementBlueScore(false)">Add</button>
            <button @click="incrementBlueScore(true)">Sub</button>
          </div>
        </div>
        <h1 style="color: lightBlue;">{{ blueScore }}</h1>
        <h1>============</h1>
        <h1 style="color: lightBlue;">{{ blueTwoScore }}</h1>
        <div class="score_two_box">
            <h1>Blue Two Score</h1>
            <input type="number" name="red_manual_scoring" ref="blue_two_input" min="0">
            <div class="choices">
              <button @click="incrementBlueTwoScore(false)">Add</button>
              <button @click="incrementBlueTwoScore(true)">Sub</button>
            </div>
        </div>
      </div>
    </div>
  `,
};
