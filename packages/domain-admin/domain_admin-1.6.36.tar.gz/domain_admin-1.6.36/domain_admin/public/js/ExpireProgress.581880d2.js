import{e as r}from"./element-plus.af689926.js";import{_ as p}from"./index.9e59753f.js";import{ah as c,o as s,c as n,O as l,S as d,a,F as _,U as o}from"./vendor-vue.cefe3aef.js";const m={name:"ExpireProgress",props:{startTime:{type:String},endTime:{type:String},isManual:{type:Boolean}},components:{},data(){return{nowTime:r()}},computed:{parsedStartTime(){return r(this.startTime)},parsedEndTime(){return r(this.endTime)},totalDays(){return this.parsedEndTime.diff(this.parsedStartTime,"day")},expireDays(){return this.parsedEndTime.diff(this.nowTime,"day")},percentage(){let e=null;return this.expireDays&&this.totalDays&&(e=this.expireDays/this.totalDays*100),e},percentageStatus(){let e;return this.expireDays>7?e="":this.expireDays>0?e="warning":e="exception",e}},methods:{async getData(){}},created(){this.getData()}},y={class:"ExpireProgress"},g={class:"ExpireProgress__info"},h={class:"el-text-color-primary"},u=a("span",null," / ",-1),x={class:"el-text-color-secondary"},f={key:1};function D(e,T,E,S,k,t){const i=c("el-progress");return s(),n("div",y,[t.percentage?(s(),l(i,{key:0,percentage:t.percentage,"show-text":!1,status:t.percentageStatus},null,8,["percentage","status"])):d("",!0),a("div",g,[t.totalDays?(s(),n(_,{key:0},[a("span",h,o(t.expireDays),1),u,a("span",x,o(t.totalDays),1)],64)):(s(),n("span",f,"-"))])])}const w=p(m,[["render",D]]);export{w as E};
