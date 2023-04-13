const mongoose=require("mongoose")

mongoose.connect("mongodb://localhost:27017/Loginsignup")
.then(()=>{
    console.log("mongodb connected")
})
.catch(()=>{
    console.log("Failed to connect")
})

const loginSchema=mongoose.Schema({
    name:{
        type : String,
        required: true
    },
    password:{
        type : String,
        required: true
    }
})

const collection=new mongoose.model("collection1",loginSchema)
module.exports=collection