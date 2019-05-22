<template>
    <div id="wrapper" class="cle">
        <div class="here cle">
            <a href="" @click="toLogin">重新登陆</a>
            <code>></code>
            员工管理中心
        </div>
        <div class="my_nala_main">
            <staffmember-menu></staffmember-menu>
            <router-view></router-view>
        </div>
    </div>
</template>
<script>
import staffmemberMenu from './staffmember-menu';
    export default {
        data () {
            return {
                
            };
        },
        props: {
            
        },
        components: {
            'staffmember-menu': staffmemberMenu,
            // 'receive': receive
        },
        created () {
            
        },
        watch: {
            
        },
        computed: {

        },
        methods: {
            toLogin () { //回到首页
                this.$router.push({name: 'login'});
            }
        }
    }
</script>
<style scoped>


.my_nala_main h3.my_nala {
    height:60px;
    border:1px solid #e7e7e7;
    border-bottom:0
}
.my_nala_main h3.my_nala a {
    display:block;
    height:60px;
    font-size:22px;
    text-align:center;
    line-height:60px;
    overflow:hidden
}
.my_nala_main h3.my_nala a:hover {
    text-decoration:none
}

</style>
