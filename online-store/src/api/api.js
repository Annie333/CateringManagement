import axios from 'axios';


let host = 'http://shop.projectsedu.com';
// let host = 'http://127.0.0.1:8000';
let local_host='http://127.0.0.1:8000';

//获取商品类别信息
export const queryCategorygoods = params => { return axios.get(`${local_host}/indexgoods/`) }

//获取首页中的新品
export const newGoods = params => { return axios.get(`${local_host}/newgoods/`) }

//获取轮播图
export const bannerGoods = params => { return axios.get(`${host}/banners/`) }

//获取商品类别信息
export const getCategory = params => {
  if('id' in params){
    return axios.get(`${local_host}/categorys/`+params.id+'/');
  }
  else{
    return axios.get(`${local_host}/categorys/`, params);
  }
};

//获取商品列表
export const getGoods = params => { 
  if('windows__id' in params){
    return axios.get(`${local_host}/goods/`+params.window__id+'/')
  }
  // else if('id' in params){
  //   return axios.get(`${local_host}/goods/`+params.id+'/')
  // }
  else{
    return axios.get(`${local_host}/goods/`, { params: params }) }
}

//获取热门搜索关键词
export const getHotSearch = params => { return axios.get(`${local_host}/hotsearchs/`) }

//获取窗口
export const getWindows = params => {
  if('id' in params){
    return axios.get(`${local_host}/windows/`+params.id+'/');
  }
  else {
    return axios.get(`${local_host}/windows/`, params);
  }
};


//商品详情
export const getGoodsDetail = goodId => { return axios.get(`${local_host}/goods/${goodId}`+'/') } //为什么要=goolid呀后端直接在url加id就可以过滤

//获取购物车商品
export const getShopCarts = params => { return axios.get(`${host}/shopcarts/`) }
// 添加商品到购物车
export const addShopCart = params => { return axios.post(`${host}/shopcarts/`, params) }
//更新购物车商品信息
export const updateShopCart = (goodsId, params) => { return axios.patch(`${host}/shopcarts/`+goodsId+'/', params) }
//删除某个商品的购物记录
export const deleteShopCart = goodsId => { return axios.delete(`${host}/shopcarts/`+goodsId+'/') }

//收藏商品
export const addGoodsFav = params => { return axios.post(`${local_host}/goodsfav/`, params) }

//取消收藏商品
export const delGoodsFav = goodsId => { return axios.delete(`${local_host}/goodsfav/`+goodsId+'/') }

export const getAllGoodsFav = () => { return axios.get(`${local_host}/goodsfav/`) }

//判断是否收藏
export const getGoodsFav = goodsId => { return axios.get(`${local_host}/goodsfav/`+goodsId+'/') }

// //收藏窗口
// export const addWindowsFav = params => { return axios.post(`${local_host}/windowsfav/`, params) }

// //取消收藏窗口
// export const delWindowsFav = windowsId => { return axios.delete(`${local_host}/windowsfav/`+windowsId+'/') }

// export const getAllWindowsFav = () => { return axios.get(`${local_host}/windowsfav/`) }

// //判断是否收藏
// export const getWindowsFav = windowsId => { return axios.get(`${local_host}/windowsfav/`+windowsId+'/') }

//登录
export const login = params => {
  return axios.post(`${local_host}/login/`, params)
}

//注册

export const register = parmas => { return axios.post(`${local_host}/users/`, parmas) }

// //短信
// export const getMessage = parmas => { return axios.post(`${host}/code/`, parmas) }


//获取用户信息
export const getUserDetail = () => { return axios.get(`${host}/users/1/`) }

//修改用户信息
export const updateUserInfo = params => { return axios.patch(`${host}/users/1/`, params) }


//获取订单
export const getOrders = () => { return axios.get(`${host}/orders/`) }
//删除订单
export const delOrder = orderId => { return axios.delete(`${host}/orders/`+orderId+'/') }
//添加订单
export const createOrder = params => {return axios.post(`${host}/orders/`, params)}
//获取订单详情
export const getOrderDetail = orderId => {return axios.get(`${host}/orders/`+orderId+'/')}


//获取留言
export const getMessages = () => {return axios.get(`${local_host}/messages/`)}

//添加留言
export const addMessage = params => {return axios.post(`${local_host}/messages/`, params, {headers:{ 'Content-Type': 'multipart/form-data' }})}

//删除留言
export const delMessages = messageId => {return axios.delete(`${local_host}/messages/`+messageId+'/')}

//添加收货地址
export const addAddress = params => {return axios.post(`${local_host}/address/`, params)}

//删除收货地址
export const delAddress = addressId => {return axios.delete(`${local_host}/address/`+addressId+'/')}

//修改收货地址
export const updateAddress = (addressId, params) => {return axios.patch(`${local_host}/address/`+addressId+'/', params)}

//获取收货地址
export const getAddress = () => {return axios.get(`${local_host}/address/`)}
