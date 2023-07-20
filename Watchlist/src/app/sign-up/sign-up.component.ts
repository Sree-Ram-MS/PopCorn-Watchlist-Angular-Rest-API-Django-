import { Component } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { DataService } from '../ser/data.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-sign-up',
  templateUrl: './sign-up.component.html',
  styleUrls: ['./sign-up.component.css']
})
export class SignUpComponent {

  backgroundImages = ['Baba.jpg','bg.jpg','iver.jpg','lala.jpeg','Loki.jpg'];

  currentBackgroundImage!: string;

  constructor( private fb:FormBuilder , private ds: DataService , private rt:Router){
    this.shuffleBackgroundImages();
    this.changeBackgroundImage();
  }

  signform = this.fb.group({
    username:['',[Validators.required,Validators.pattern("[a-zA-Z 0-9]+")]],
    password:['',[Validators.required,Validators.minLength(2)]],
    password2:['',[Validators.required,Validators.minLength(2)]],
    email:['',[Validators.required,Validators.email]],
  })

  register(){
    const { username, email, password, password2 }  = this.signform.value;

    if ( username && email && password && password2 ) {
      this.ds.signin( username , email ,password ,password2)
        .then(res => res.json())
        .then (data => { 
        console.log( data);
      });
      this.rt.navigate([''])
    } else {
      console.log("error");
    }
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
