import React, { useState } from 'react';
import { DatePicker, DatePickerValue } from "@tremor/react";

interface Props {
  date: Date;
  setDate: (date: Date) => void;
}

export default function Header({date, setDate}: Props) {
    return (
        <div className="flex-col items-center justify-center mt-10 sm:mt-20">
          <div className="flex items-center font-bold text-2xl">
            <span className="w-full">Today's date is</span>
            <div className="w-64">
              <DatePicker 
                className="font-bold text-xl" 
                value={date} 
                onValueChange={(newDate: DatePickerValue) => {
                  if (newDate) {
                    setDate(newDate);
                  }
                }} 
                enableClear={false} 
              />
            </div>
          </div>
        </div>
    )
}