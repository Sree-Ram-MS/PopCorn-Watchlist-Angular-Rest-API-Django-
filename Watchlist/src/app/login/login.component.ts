import { Component } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { DataService } from '../ser/data.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {

  backgroundImages = ['Baba.jpg','bg.jpg','iver.jpg','lala.jpeg','Loki.jpg'];

  currentBackgroundImage!: string;


  constructor(private fb:FormBuilder, private ds:DataService ,private rt:Router) {
    this.shuffleBackgroundImages();
    this.changeBackgroundImage();
  }




  loginform = this.fb.group ({
    username:['',[Validators.pattern("[a-zZ-Z 0-9]+")]],
    password:['',[Validators.minLength(2)]]
  })

  clicked(){
    this.ds.login(this.loginform.value).then(res=> res.json()).then(data=>{
      console.log(data)
      if ( data["token"]){
        localStorage.setItem('token',data['token'])
        this.rt.navigate(['Nav'])
        alert("login success")
      }
      else {
        alert("error")
      }
    })
  }
  shuffleBackgroundImages() {
    for ( let i= this.backgroundImages.length - 1; i > 0 ; i-- ) {
      const j = Math.floor(Math.random() * (i+ 1));
      [this.backgroundImages[i],this.backgroundImages[j]]= [this.backgroundImages[j],this.backgroundImages[i]];
    }
  }

  changeBackgroundImage () {
    this.currentBackgroundImage = this.backgroundImages[0];

    setInterval(() => {
      const currentIndex = this.backgroundImages.indexOf(this.currentBackgroundImage);
      const nextIndex = ( currentIndex + 1 ) % this.backgroundImages.length;
      this.currentBackgroundImage = this.backgroundImages[nextIndex];
    },5000);
  }

}
