import{t as R,_ as S}from"./index.9e59753f.js";import{ah as i,o as c,O as y,P as a,V as l,c as v,F as E,a8 as $,a as g,S as k,T as x,U as f,ax as I,ar as q,Q as B,a9 as j}from"./vendor-vue.cefe3aef.js";import{C as K}from"./ConnectStatus.60fff513.js";import{M as W}from"./monitor-status-enums.ebbc2064.js";import{D as Q}from"./DataCount.e5cdbb0d.js";import{C as J,E as X}from"./ExportFileDialog.730446f7.js";import{u as Y}from"./group-store.6ec1d3f3.js";import{F as Z}from"./vendor-lib.a8c0b8df.js";import{d as ee}from"./element-plus.af689926.js";import"./element-icon.1fe9d2a8.js";const te={title:[{message:"\u540D\u79F0\u4E0D\u80FD\u4E3A\u7A7A",required:!0,trigger:"blur"}],monitor_type:[{message:"\u76D1\u63A7\u7C7B\u578B\u4E0D\u80FD\u4E3A\u7A7A",required:!0,trigger:"blur"}],interval:[{message:"\u68C0\u6D4B\u9891\u7387\u4E0D\u80FD\u4E3A\u7A7A",required:!0,trigger:"blur"}],allow_error_count:[{message:"\u91CD\u8BD5\u6B21\u6570\u4E0D\u80FD\u4E3A\u7A7A",required:!0,trigger:"blur"}]},T={UNKNOWN:0,HTTP:1},O=[{value:T.HTTP,label:R("HTTP")}],le=[{value:T.UNKNOWN,label:R("\u672A\u77E5")},...O];function oe(t){var e;return(e=le.find(o=>o.value==t))==null?void 0:e.label}const ne={GET:"GET",POST:"POST"},U=[{value:ne.GET,label:R("GET")}],ie={url:[{message:"URL\u4E0D\u80FD\u4E3A\u7A7A",required:!0,trigger:"blur"}],method:[{message:"\u8BF7\u6C42\u65B9\u5F0F\u4E0D\u80FD\u4E3A\u7A7A",required:!0,trigger:"blur"}],timeout:[{message:"\u8D85\u65F6\u65F6\u95F4\u4E0D\u80FD\u4E3A\u7A7A",required:!0,trigger:"blur"}]},ae={name:"",props:{form:{type:Object,default:null}},components:{},data(){return{rules:ie,MonitorTypeEnum:T,MonitorTypeOptions:O,RequestMethodOptions:U}},computed:{},methods:{handleSubmit(){console.log("handleSubmit"),this.$refs.form.validate(t=>{if(console.log(t),t)this.confirmSubmit();else return!1})},confirmSubmit(){console.debug("confirmSubmit",this.form),this.$emit("on-confirm",this.form)}},created(){}},re=g("span",{class:"ml-sm color--info"},"\uFF08\u79D2\uFF09",-1);function se(t,e,o,_,n,r){const u=i("el-option"),d=i("el-select"),h=i("el-form-item"),C=i("el-input"),D=i("el-form");return c(),y(D,{ref:"form",model:o.form,rules:n.rules,"label-width":"100px"},{default:a(()=>[l(h,{label:"\u8BF7\u6C42\u65B9\u5F0F",prop:"method"},{default:a(()=>[l(d,{modelValue:o.form.method,"onUpdate:modelValue":e[0]||(e[0]=m=>o.form.method=m),style:{width:"140px"},disabled:""},{default:a(()=>[(c(!0),v(E,null,$(n.RequestMethodOptions,m=>(c(),y(u,{key:m.value,label:m.label,value:m.value},null,8,["label","value"]))),128))]),_:1},8,["modelValue"])]),_:1}),l(h,{label:"\u8BF7\u6C42URL",prop:"url"},{default:a(()=>[l(C,{type:"text",modelValue:o.form.url,"onUpdate:modelValue":e[1]||(e[1]=m=>o.form.url=m),placeholder:"\u8BF7\u8F93\u5165\u8BF7\u6C42URL"},null,8,["modelValue"])]),_:1}),l(h,{label:"\u8BF7\u6C42\u8D85\u65F6",prop:"timeout"},{default:a(()=>[l(C,{style:{width:"140px"},type:"number",modelValue:o.form.timeout,"onUpdate:modelValue":e[2]||(e[2]=m=>o.form.timeout=m),placeholder:"\u8BF7\u8F93\u5165\u8D85\u65F6\u65F6\u95F4"},null,8,["modelValue"]),re]),_:1})]),_:1},8,["model","rules"])}const ue=S(ae,[["render",se]]),de={name:"",props:{row:{type:Object,default:null}},components:{HttpDataForm:ue},data(){return{rules:te,MonitorTypeEnum:T,MonitorTypeOptions:O,RequestMethodOptions:U,form:{title:"",monitor_type:O[0].value,content:{method:U[0].value,url:"",timeout:3},interval:"60",status:"",is_active:!0,next_run_time:"",allow_error_count:"0"}}},computed:{},methods:{async getData(){if(this.row){let t={monitor_id:this.row.id};const e=await this.$http.getMonitorById(t);if(e.code!=0)return;let o=e.data;this.form.title=o.title,this.form.monitor_type=o.monitor_type,this.form.content=o.content,this.form.interval=o.interval,this.form.allow_error_count=o.allow_error_count}},handleCancel(){this.$emit("on-cancel")},handleSubmit(){this.$refs.MonitorDataForm.handleSubmit()},handleMonitorDataFormConfirm(){this.$refs.form.validate(t=>{if(t)this.confirmSubmit();else return!1})},async confirmSubmit(){console.log("handleMonitorDataFormConfirm");let t=this.$loading({fullscreen:!0}),e={title:this.form.title,monitor_type:this.form.monitor_type,content:this.form.content,interval:this.form.interval,allow_error_count:this.form.allow_error_count},o=null;this.row&&this.row.id?o=await this.$http.updateMonitorById({...e,monitor_id:this.row.id}):o=await this.$http.addMonitor(e),o.code==0?(this.$msg.success("\u64CD\u4F5C\u6210\u529F"),this.$emit("on-success")):this.$msg.error(o.msg),this.$nextTick(()=>{t.close()})}},created(){this.getData()}},ce=g("span",{class:"color--info ml-sm"},"\uFF08\u5206\u949F\uFF09",-1),me={class:"text-center"};function pe(t,e,o,_,n,r){const u=i("el-input"),d=i("el-form-item"),h=i("el-option"),C=i("el-select"),D=i("HttpDataForm"),m=i("el-form"),F=i("el-button");return c(),v("div",null,[l(m,{ref:"form",model:n.form,rules:n.rules,"label-width":"100px"},{default:a(()=>[l(d,{label:"\u540D\u79F0",prop:"title"},{default:a(()=>[l(u,{type:"text",modelValue:n.form.title,"onUpdate:modelValue":e[0]||(e[0]=p=>n.form.title=p),placeholder:"\u8BF7\u8F93\u5165\u540D\u79F0"},null,8,["modelValue"])]),_:1}),l(d,{label:"\u76D1\u63A7\u7C7B\u578B",prop:"monitor_type"},{default:a(()=>[l(C,{modelValue:n.form.monitor_type,"onUpdate:modelValue":e[1]||(e[1]=p=>n.form.monitor_type=p),style:{width:"140px"},disabled:""},{default:a(()=>[(c(!0),v(E,null,$(n.MonitorTypeOptions,p=>(c(),y(h,{key:p.value,label:p.label,value:p.value},null,8,["label","value"]))),128))]),_:1},8,["modelValue"])]),_:1}),n.MonitorTypeEnum.HTTP==n.form.monitor_type?(c(),y(D,{key:0,ref:"MonitorDataForm",form:n.form.content,onOnConfirm:r.handleMonitorDataFormConfirm},null,8,["form","onOnConfirm"])):k("",!0),l(d,{label:"\u68C0\u6D4B\u9891\u7387",prop:"interval"},{default:a(()=>[l(u,{style:{width:"140px"},type:"number",modelValue:n.form.interval,"onUpdate:modelValue":e[2]||(e[2]=p=>n.form.interval=p),placeholder:"\u8BF7\u8F93\u5165\u68C0\u6D4B\u9891\u7387"},null,8,["modelValue"]),ce]),_:1}),l(d,{label:"\u91CD\u8BD5\u6B21\u6570",prop:"allow_error_count"},{default:a(()=>[l(u,{style:{width:"140px"},type:"number",modelValue:n.form.allow_error_count,"onUpdate:modelValue":e[3]||(e[3]=p=>n.form.allow_error_count=p),placeholder:"\u8BF7\u8F93\u5165\u91CD\u8BD5\u6B21\u6570"},null,8,["modelValue"])]),_:1})]),_:1},8,["model","rules"]),g("div",me,[l(F,{onClick:r.handleCancel},{default:a(()=>[x(f(t.$t("\u53D6\u6D88")),1)]),_:1},8,["onClick"]),l(F,{type:"primary",onClick:r.handleSubmit},{default:a(()=>[x(f(t.$t("\u786E\u5B9A")),1)]),_:1},8,["onClick"])])])}const he=S(de,[["render",pe]]),_e={name:"",props:{row:{type:Object,default:null},visible:{type:Boolean,default:!1}},emits:["update:visible"],components:{DataForm:he},data(){return{}},computed:{dialogTitle(){return this.row?"\u7F16\u8F91":"\u6DFB\u52A0"},dialogVisible:{get(){return this.visible},set(t){this.$emit("update:visible",t)}}},methods:{handleClose(){this.$emit("update:visible",!1)},handleOpen(){this.$emit("update:visible",!0)},handleSuccess(){this.handleClose(),this.$emit("on-success")}},created(){}};function fe(t,e,o,_,n,r){const u=i("DataForm"),d=i("el-dialog");return c(),y(d,{title:r.dialogTitle,modelValue:r.dialogVisible,"onUpdate:modelValue":e[0]||(e[0]=h=>r.dialogVisible=h),width:"600px",center:"","append-to-body":""},{default:a(()=>[r.dialogVisible?(c(),y(u,{key:0,row:o.row,onOnCancel:r.handleClose,onOnSuccess:r.handleSuccess},null,8,["row","onOnCancel","onOnSuccess"])):k("",!0)]),_:1},8,["title","modelValue"])}const P=S(_e,[["render",fe]]),ge={name:"",components:{DataFormDialog:P,ConnectStatus:K},props:{list:{type:Array}},computed:{},data(){return{currentRow:null,dialogVisible:!1}},methods:{handleEditRow(t){this.currentRow=t,this.dialogVisible=!0},async handleDeleteClick(t){let e={monitor_id:t.id};const o=await this.$http.removeMonitorById(e);o.code==0?(this.$msg.success("\u64CD\u4F5C\u6210\u529F"),this.$emit("on-success")):this.$msg.error(o.msg)},async handleStatusChange(t,e){let o={monitor_id:t.id,is_active:e};const _=await this.$http.updateMonitorActive(o);_.code==0?(this.$msg.success("\u64CD\u4F5C\u6210\u529F"),this.$emit("on-success")):this.$msg.error(_.msg)},handleUpdateSuccess(){this.$emit("on-success")},handleOpenLogClick(t){let e=this.$router.resolve({name:"log-monitor-list",query:{monitorId:t.id}});window.open(e.href,"_blank")},handleSelectable(t,e){return!0}},created(){}},be={key:1};function we(t,e,o,_,n,r){const u=i("el-table-column"),d=i("ConnectStatus"),h=i("el-link"),C=i("el-switch"),D=i("Edit"),m=i("el-icon"),F=i("Delete"),p=i("el-popconfirm"),V=i("el-table"),M=i("DataFormDialog");return c(),v("div",null,[l(V,{data:o.list,stripe:"",border:"",onSelectionChange:e[0]||(e[0]=s=>t.$emit("selection-change",s))},{default:a(()=>[l(u,{type:"selection","header-align":"center",align:"center",width:"40",selectable:r.handleSelectable},null,8,["selectable"]),l(u,{label:t.$t("\u540D\u79F0"),"header-align":"center",align:"center",prop:"title"},{default:a(s=>[g("span",null,f(s.row.title||"-"),1)]),_:1},8,["label"]),l(u,{label:t.$t("\u76D1\u63A7\u7C7B\u578B"),"header-align":"center",align:"center",prop:"monitor_type",width:"100"},{default:a(s=>[g("span",null,f(s.row.monitor_type_label||"-"),1)]),_:1},8,["label"]),l(u,{label:t.$t("\u9891\u7387(\u5206\u949F)"),"header-align":"center",align:"center",prop:"interval",width:"120"},{default:a(s=>[g("span",null,f(s.row.interval||"-"),1)]),_:1},8,["label"]),l(u,{label:t.$t("\u72B6\u6001"),"header-align":"center",align:"center",prop:"status",width:"100"},{default:a(s=>[l(d,{value:s.row.status_value,onOnClick:b=>r.handleOpenLogClick(s.row)},null,8,["value","onOnClick"])]),_:1},8,["label"]),l(u,{label:t.$t("\u65E5\u5FD7"),"header-align":"center",align:"center",prop:"interval",width:"100"},{default:a(s=>[s.row.log_count&&s.row.log_count>0?(c(),y(h,{key:0,underline:!1,onClick:b=>r.handleOpenLogClick(s.row)},{default:a(()=>[x(f(s.row.log_count),1)]),_:2},1032,["onClick"])):(c(),v("span",be,"-"))]),_:1},8,["label"]),l(u,{label:t.$t("\u4E0B\u6B21\u8FD0\u884C\u65F6\u95F4"),"header-align":"center",align:"center",prop:"next_run_time",width:"180"},{default:a(s=>[g("span",null,f(s.row.next_run_time||"-"),1)]),_:1},8,["label"]),l(u,{label:t.$t("\u542F\u7528"),"header-align":"center",align:"center",width:"80"},{default:a(s=>[l(C,{modelValue:s.row.is_active,"onUpdate:modelValue":b=>s.row.is_active=b,onChange:b=>r.handleStatusChange(s.row,b)},null,8,["modelValue","onUpdate:modelValue","onChange"])]),_:1},8,["label"]),l(u,{label:t.$t("\u64CD\u4F5C"),width:"80","header-align":"center",align:"center"},{default:a(s=>[l(h,{underline:!1,type:"primary",class:"mr-sm",onClick:b=>r.handleEditRow(s.row)},{default:a(()=>[l(m,null,{default:a(()=>[l(D)]),_:1})]),_:2},1032,["onClick"]),l(p,{title:`${t.$t("\u786E\u5B9A\u5220\u9664")}\uFF1F`,onConfirm:b=>r.handleDeleteClick(s.row)},{reference:a(()=>[l(h,{underline:!1,type:"danger"},{default:a(()=>[l(m,null,{default:a(()=>[l(F)]),_:1})]),_:1})]),_:2},1032,["title","onConfirm"])]),_:1},8,["label"])]),_:1},8,["data"]),l(M,{visible:n.dialogVisible,"onUpdate:visible":e[1]||(e[1]=s=>n.dialogVisible=s),row:n.currentRow,onOnSuccess:r.handleUpdateSuccess},null,8,["visible","row","onOnSuccess"])])}const ye=S(ge,[["render",we]]),Ce={name:"ConditionFilter",props:{},components:{ConditionFilterGroup:J},data(){return{loading:!0,options:[{title:"\u7F51\u7AD9\u72B6\u6001",field:"status",selected:[],maxCount:1,options:[{label:"\u8FDE\u63A5\u5F02\u5E38",value:2},{label:"\u8FDE\u63A5\u6B63\u5E38",value:1},{label:"\u72B6\u6001\u672A\u77E5",value:0}]}]}},computed:{...I(Y,{groupOptions:"getGroupOptions"})},methods:{async resetData(){const t=await this.$http.getGroupList();t.ok&&this.options.forEach(e=>{e.field=="group_ids"&&(t.data.list&&t.data.list.length>0?(e.options=t.data.list.map(o=>{let _=o.name;return{...o,value:o.id,label:_}}),e.hidden=!1):e.hidden=!0)}),this.loading=!1},handleChange(t){this.$emit("on-change",this.options)}},created(){this.loading=!1}},ve={class:""};function De(t,e,o,_,n,r){const u=i("ConditionFilterGroup"),d=q("loading");return B((c(),v("div",ve,[l(u,{options:n.options,onOnChange:r.handleChange},null,8,["options","onOnChange"])])),[[d,n.loading]])}const xe=S(Ce,[["render",De]]),Fe={name:"monitor-list",props:{},components:{DataFormDialog:P,DataTable:ye,DataCount:Q,ConditionFilter:xe,ExportFileDialog:X},data(){return{list:[],total:0,page:1,size:20,keyword:"",timer:null,loading:!0,hasInitData:!0,dialogVisible:!1,params:{},ConditionFilterParams:[],exportFileDialogVisible:!1,next_run_time:null,selectedRows:[]}},computed:{showBatchActionButton(){return!!(this.selectedRows&&this.selectedRows.length>0)}},methods:{resetData(){this.page=1,this.getData()},async getMonitorTaskNextRunTime(){const t=await this.$http.getMonitorTaskNextRunTime();this.next_run_time=t.data.next_run_time},async getData(){this.loading=!0;let t={page:this.page,size:this.size,keyword:this.keyword};for(let e of this.ConditionFilterParams)e.selected&&e.selected.length>0&&(e.maxCount==1?t[e.field]=e.selected[0]:t[e.field]=e.selected);this.params=t;try{const e=await this.$http.getMonitorList(t);e.code==0&&(this.list=e.data.list.map(o=>(o.monitor_type_label=oe(o.monitor_type),o.status_value=W(o.status),o)),this.total=e.data.total)}catch(e){console.log(e)}finally{this.loading=!1}},handleAddRow(){this.dialogVisible=!0},handleAddSuccess(){this.resetData()},handleSearch(){this.resetData()},handleConditionFilterChange(t){console.log(t),this.ConditionFilterParams=t,this.resetData()},handleExportToFile(){this.exportFileDialogVisible=!0},async handleExportConfirm(t){const e=await this.$http.exportMonitorFile({...this.params,ext:t.ext});e.ok&&Z.saveAs(e.data.url,e.data.name)},handleExceed(t){this.$refs.upload.clearFiles();const e=t[0];e.uid=ee(),this.handleHttpRequest({file:e})},async handleHttpRequest(t){let e=this.$loading({fullscreen:!0}),o=new FormData;o.append("file",t.file),(await this.$http.importMonitorFromFile(o)).code==0&&(this.$msg.success("\u5BFC\u5165\u6210\u529F\uFF0C\u540E\u53F0\u68C0\u6D4B\u4E2D"),this.resetData(),this.$refs.ConditionFilter&&this.$refs.ConditionFilter.resetData()),e.close()},handleSelectionChange(t){this.selectedRows=t},async handleBatchDeleteConfirm(){let t=this.$loading({fullscreen:!0}),e={monitor_ids:this.selectedRows.map(o=>o.id)};try{const o=await this.$http.deleteMonitorByIds(e);o.code==0?(this.$msg.success("\u64CD\u4F5C\u6210\u529F"),this.resetData()):this.$msg.error(o.msg)}catch(o){console.log(o)}finally{this.$nextTick(()=>{t.close()})}}},beforeUnmount(){this.timer&&(clearInterval(this.timer),this.timer=null)},created(){this.resetData()}},Se={class:"app-container"},Ve={class:"flex justify-between"},ke={class:"flex mt-sm",style:{"align-items":"center"}},Oe={class:"flex",style:{"margin-left":"auto"}},Te={key:0,class:"color--info text-sm"},Me=g("div",{style:{position:"absolute",top:"0",left:"0",right:"0",bottom:"0"}},null,-1);function Ue(t,e,o,_,n,r){const u=i("Plus"),d=i("el-icon"),h=i("el-button"),C=i("Search"),D=i("el-input"),m=i("ConditionFilter"),F=i("DataCount"),p=i("Delete"),V=i("el-link"),M=i("el-popconfirm"),s=i("Upload"),b=i("el-upload"),N=i("Download"),G=i("DataTable"),H=i("el-pagination"),A=i("DataFormDialog"),L=i("ExportFileDialog"),z=q("loading");return c(),v("div",Se,[g("div",Ve,[l(h,{type:"primary",onClick:r.handleAddRow},{default:a(()=>[l(d,null,{default:a(()=>[l(u)]),_:1}),x(f(t.$t("\u6DFB\u52A0")),1)]),_:1},8,["onClick"]),l(D,{class:"ml-sm",style:{width:"260px"},modelValue:n.keyword,"onUpdate:modelValue":e[0]||(e[0]=w=>n.keyword=w),placeholder:"\u8F93\u5165\u540D\u79F0",clearable:"",onKeypress:j(r.handleSearch,["enter"]),onClear:r.handleSearch},{append:a(()=>[l(h,{onClick:r.handleSearch},{default:a(()=>[l(d,null,{default:a(()=>[l(C)]),_:1})]),_:1},8,["onClick"])]),_:1},8,["modelValue","onKeypress","onClear"])]),n.hasInitData?(c(),y(m,{key:0,class:"mt-md",ref:"ConditionFilter",onOnChange:r.handleConditionFilterChange},null,8,["onOnChange"])):k("",!0),g("div",ke,[l(F,{value:n.total},null,8,["value"]),g("div",Oe,[n.next_run_time?(c(),v("span",Te,"\u5373\u5C06\u8FD0\u884C\uFF1A"+f(n.next_run_time),1)):k("",!0),r.showBatchActionButton?(c(),y(M,{key:1,title:"\u786E\u5B9A\u5220\u9664\u9009\u4E2D\uFF1F",onConfirm:r.handleBatchDeleteConfirm},{reference:a(()=>[l(V,{underline:!1,type:"danger",class:"ml-sm"},{default:a(()=>[l(d,null,{default:a(()=>[l(p)]),_:1}),x("\u6279\u91CF\u5220\u9664")]),_:1})]),_:1},8,["onConfirm"])):k("",!0),l(V,{underline:!1,type:"primary",class:"ml-sm",style:{position:"relative"}},{default:a(()=>[l(d,null,{default:a(()=>[l(s)]),_:1}),x(f(t.$t("\u5BFC\u5165"))+" ",1),l(b,{ref:"upload",action:"action",accept:".txt,.csv,.xlsx",limit:1,"on-exceed":r.handleExceed,"show-file-list":!1,"http-request":r.handleHttpRequest},{default:a(()=>[Me]),_:1},8,["on-exceed","http-request"])]),_:1}),l(V,{underline:!1,type:"primary",class:"ml-sm",onClick:r.handleExportToFile},{default:a(()=>[l(d,null,{default:a(()=>[l(N)]),_:1}),x(f(t.$t("\u5BFC\u51FA")),1)]),_:1},8,["onClick"])])]),B(l(G,{class:"mt-sm",list:n.list,onOnSuccess:r.resetData,onSelectionChange:r.handleSelectionChange},null,8,["list","onOnSuccess","onSelectionChange"]),[[z,n.loading]]),l(H,{class:"mt-md justify-center",background:"",layout:"total, prev, pager, next",total:n.total,"page-size":n.size,"onUpdate:pageSize":e[1]||(e[1]=w=>n.size=w),"current-page":n.page,"onUpdate:currentPage":e[2]||(e[2]=w=>n.page=w),onCurrentChange:r.getData},null,8,["total","page-size","current-page","onCurrentChange"]),l(A,{visible:n.dialogVisible,"onUpdate:visible":e[3]||(e[3]=w=>n.dialogVisible=w),onOnSuccess:r.handleAddSuccess},null,8,["visible","onOnSuccess"]),l(L,{allowExts:["xlsx","csv"],visible:n.exportFileDialogVisible,"onUpdate:visible":e[4]||(e[4]=w=>n.exportFileDialogVisible=w),onOnConfirm:r.handleExportConfirm},null,8,["visible","onOnConfirm"])])}const Le=S(Fe,[["render",Ue]]);export{Le as default};
